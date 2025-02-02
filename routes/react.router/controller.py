import markupsafe

paths = wiz.request.segment.path.split("/")
app = wiz.model("react/main")("build").load("")

if paths[0] == "build":
    filename = paths[-1]
    ext = filename.split(".")[-1]
    extmap = {
        "js": "javascript",
        "css": "css",
    }
    res = ""
    try:
        res = app.fs.read.text(f"wiz.build.{ext}")
    except:
        pass
    wiz.response.send(res, "text/"+extmap[ext])

view = app.fs.read.text("wiz.build.html")
view = markupsafe.Markup(view)
wiz.response.send(view, "text/html")
