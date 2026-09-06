import os
import json

def get_folder_size(path):
    total = 0
    try:
        for entry in os.scandir(path):
            if entry.is_file(follow_symlinks=False):
                total += entry.stat().st_size
            elif entry.is_dir(follow_symlinks=False):
                total += get_folder_size(entry.path)
    except:
        pass
    return total


def scan_folder(path):
    items = []

    for entry in os.scandir(path):
        try:
            if entry.is_file(follow_symlinks=False):
                size = entry.stat().st_size
                items.append({
                    "name": entry.name,
                    "type": "file",
                    "size": size
                })

            elif entry.is_dir(follow_symlinks=False):
                size = get_folder_size(entry.path)
                children = scan_folder(entry.path)

                items.append({
                    "name": entry.name,
                    "type": "folder",
                    "size": size,
                    "children": children
                })
        except:
            pass

    items.sort(key=lambda x: x["size"], reverse=True)
    return items


def format_size(size):
    for unit in ["B","KB","MB","GB","TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024


def generate_html(data, total):

    html = f"""
<html>
<head>

<style>

body {{
    font-family: Arial;
    background:#111;
    color:white;
}}

ul {{
    list-style:none;
}}

.folder {{
    cursor:pointer;
}}

.bar {{
    display:inline-block;
    height:10px;
    background:lime;
}}

.size {{
    color:lightblue;
}}

.percent {{
    color:orange;
}}

</style>

<script>

function toggle(id){{
    let e=document.getElementById(id)
    if(e.style.display==="none")
        e.style.display="block"
    else
        e.style.display="none"
}}

</script>

</head>
<body>

<h2>Disk Usage Analyzer</h2>

"""

    counter = 0

    def render(items, depth=0):
        nonlocal counter
        html_part = "<ul>"

        for item in items:

            percent = (item["size"]/total)*100
            bar = percent*5

            if item["type"]=="folder":

                counter+=1
                cid=f"id{counter}"

                html_part+=f"""
<li class='folder' onclick="toggle('{cid}')">

📁 {item['name']} 
<span class='size'>{format_size(item['size'])}</span>
<span class='percent'>({percent:.2f}%)</span>

<div class='bar' style='width:{bar}px'></div>

</li>

<div id='{cid}' style='display:none;margin-left:20px'>
{render(item["children"],depth+1)}
</div>
"""

            else:

                html_part+=f"""
<li>

📄 {item['name']} 
<span class='size'>{format_size(item['size'])}</span>
<span class='percent'>({percent:.2f}%)</span>

<div class='bar' style='width:{bar}px'></div>

</li>
"""

        html_part+="</ul>"
        return html_part

    html+=render(data)
    html+="</body></html>"

    return html


if __name__=="__main__":

    path=input("Enter folder path to analyze: ")

    print("Scanning disk... this may take time")

    data=scan_folder(path)

    total=sum(i["size"] for i in data)

    html=generate_html(data,total)

    with open("disk_report.html","w",encoding="utf-8") as f:
        f.write(html)

    print("Report generated: disk_report.html")