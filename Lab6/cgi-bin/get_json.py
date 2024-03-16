import sqlite3
import json

db = sqlite3.connect('database.db')
c = db.cursor()

c.execute("SELECT rowid, * FROM users")
users_rows = c.fetchall()
users_result = []
for row in users_rows:
    d = {}
    for i, col in enumerate(c.description):
        d[col[0]] = row[i]
    users_result.append(d)
users_json = json.dumps(users_result, indent=2)

c.execute("SELECT rowid, * FROM vehicles")
vehicles_rows = c.fetchall()
vehicles_result = []
for row in vehicles_rows:
    d = {}
    for i, col in enumerate(c.description):
        d[col[0]] = row[i]
    vehicles_result.append(d)
vehicles_json = json.dumps(vehicles_result, indent=2)

c.execute("SELECT rowid, * FROM auto_parts")
auto_parts_rows = c.fetchall()
auto_parts_result = []
for row in auto_parts_rows:
    d = {}
    for i, col in enumerate(c.description):
        d[col[0]] = row[i]
    auto_parts_result.append(d)
auto_parts_json = json.dumps(auto_parts_result, indent=2)

db.close()
print(f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JSON</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col card bg-dark text-white my-5 mx-3" style="border-radius: 1rem;">
                <div class="card-body py-5 px-3">
                    <h5 class="fw-bold mb-3 text-uppercase">Пользователи</h5>
                    <pre id="users"></pre>
                </div>
            </div>
            <div class="col card bg-dark text-white my-5 mx-3" style="border-radius: 1rem;">
                <div class="card-body py-5 px-3">
                    <h5 class="fw-bold mb-3 text-uppercase">Транспорт</h5>
                    <pre id="vehicles"></pre>
                </div>
            </div>
            <div class="col card bg-dark text-white my-5 mx-3" style="border-radius: 1rem;">
                <div class="card-body py-5 px-3">
                    <h5 class="fw-bold mb-3 text-uppercase">Комплектующие</h5>
                    <pre id="auto_parts"></pre>
                </div>
            </div>
        </div>
    </div>
</body>

<script>
    var data = {users_json}
    document.getElementById("users").textContent = JSON.stringify(data, undefined, 2);
    
    var data = {vehicles_json}
    document.getElementById("vehicles").textContent = JSON.stringify(data, undefined, 2);
    
    var data = {auto_parts_json}
    document.getElementById("auto_parts").textContent = JSON.stringify(data, undefined, 2);
</script>
</html>""")