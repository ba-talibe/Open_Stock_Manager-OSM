#! /usr/bin/python3 
# -*-coding : utf-8 -*- 
import sys

sys.path.append("/usr/share/osm")

import core


from core import readAll

entete = "Content-type: text/html\n\n"

ligne = """<tr>
                <td>{id}</td><td>{code}</td> <td>{designation}</td><td>{descriptions}</td>
        </tr>"""

body = """
		<table border='1px'>
                       <thead>
                        <tr>
                                <th colspan=5>Articles</th>
                        </tr>
                        <tr>
                                <th>id</th>
                                <th>code</th>
                                <th>designation</th>
                                <th>descriptions</th>
                        </tr>
                        </thead>
        <tr>

        {lignes}
        </table>.
			"""

html = """
<html>
	<body>

    {body}
    </body>
</html>
"""
lignes = ""
for client in readAll():
    lignes += ligne.format(id=client[0],
                            code=client[1],
                            designation=client[2],
                            descriptions=client[3]) + "\n"

body = body.format(lignes=lignes)
html = html.format(body=body)

print(entete)
print(html)
