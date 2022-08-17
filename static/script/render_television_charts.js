let router
let url = "../static/router/television.json"
let request = new XMLHttpRequest()

request.open("get", url)
request.send(null)
request.onload = function() {
    if (request.status === 200) {
        router = JSON.parse(request.responseText)
        console.log(router.charts)
        for (let path of router.charts) {
            let newChildNode = document.createElement("div")
            newChildNode.id = path
            newChildNode.className = "chart_box"
            console.log(`render${path}`)
            document.getElementById("charts_wrapper").appendChild(newChildNode)
            document.getElementById(path).innerHTML = `<object class="chart type="text/html" data="../static/charts/television/${path}.html" width=100% height=100%></object>`
        }
    }
}

