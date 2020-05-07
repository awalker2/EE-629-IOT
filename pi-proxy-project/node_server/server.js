var express = require('express');
var fs = require('fs');

var server = express();
server.set('view engine', 'ejs');

const dbPath = '../proxy/data/db.json';

// Clear the database route
server.get('/delete', function (req, res) {
    // Try to delete DB
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    
    try {
        fs.unlinkSync(dbPath);
        res.end('DB Cleared');
    } catch (e) {
        console.log(e);
        res.end('Error clearing DB');
    }

    res.render('index', { chartData } );
});

// Main route
server.get('/', function (req, res) {
    let jsonHistory;
    // Try to open DB, if not just return empty JSON
    try {
        jsonHistory = JSON.parse(fs.readFileSync(dbPath));
    } catch (e) {
        console.log(e)
        jsonHistory = {};
    }

    // Object containing all the web history and HTML versions
    let historyObj = {};
    let httpVerObj = {};
    jsonHistory = jsonHistory._default
    for (let entry in jsonHistory) {        
        // Host info
        const host = jsonHistory[entry].host;
        const size = jsonHistory[entry].size;

        if (historyObj[host]) {
            historyObj[host].count++;
            historyObj[host].size+=size;
        } else {
            historyObj[host] = { count: 1, size: size };
        }

        // HTML info
        const httpVer = jsonHistory[entry].httpVer;
        
        if (httpVerObj[httpVer]) {
            httpVerObj[httpVer].count++;
        } else {
            httpVerObj[httpVer] = { count: 1 };
        }
    }

    // Array containing all the web history to sort
    let historyList = []
    for (let obj in historyObj) {
        historyList.push({
            'host': obj, 
            'size': historyObj[obj].size, 
            'count': historyObj[obj].count
        });
    }

    // Array containing all the HTML version info
    let httpVerList = []
    for (let obj in httpVerObj) {
        httpVerList.push({
            'name' : obj,
            'count' : httpVerObj[obj].count
        });
    }

    // Sort the list based on the count, top 10
    historyList.sort((a, b) => b.count - a.count);
    let topHostsByCount = historyList.slice(0, 10);

    // Sort the list based on the size, top 10
    historyList.sort((a, b) => b.size - a.size);
    let topHostsBySize = historyList.slice(0, 10);

    let hostLabels = topHostsByCount.map(x => x.host);
    let chartData = {
        chart1 : {
            labels: topHostsByCount.map(x => x.host),
            data: topHostsByCount.map(x => x.count)
        },
        chart2 : {
            labels: topHostsBySize.map(x => x.host),
            data: topHostsBySize.map(x => x.size)
        },
        chart3 : {
            labels: httpVerList.map(x => x.name),
            data: httpVerList.map(x => x.count)
        }
    }

    res.render('index', { chartData } );
});


// Start server
server.listen(9091, function () {
    console.log('server started on port 9091');
});