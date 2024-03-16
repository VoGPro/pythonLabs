#!/usr/cgi-bin/env python3
import sqlite3

db = sqlite3.connect('database.db')
c = db.cursor()

print("""<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Luxury Autos</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
</head>

<body class="d-flex flex-column min-vh-100">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark p-4">
        <div class="container-fluid">
            <h1 class="display-6 text-white pe-5">Luxury Autos</h1>
                <a href="get_json.py" class="btn btn-outline-primary btn-lg" type="submit">JSON</a>
            </div>
        </div>
    </nav>

    <div class="container text-center">
        <div class="row">
            <div class="col card bg-dark text-white mt-5 mx-5" style="border-radius: 1rem;">
                <div class="card-body p-5 text-center">
                    <form action="delete_user.py" method="POST">
                        <h5 class="fw-bold mb-3 text-uppercase">Пользователи</h5>
                        <label>
                            <input name="user_id" placeholder="Введите id" class="form-control" value="" required />
                        </label><br />
                        <button class="btn btn-danger mt-3">Удалить</button>
                    </form>
                </div>
            </div>
            <div class="col card bg-dark text-white mt-5 mx-5" style="border-radius: 1rem;">
                <div class="card-body p-5 text-center">
                    <form action="delete_vehicle.py" method="POST">
                        <h5 class="fw-bold mb-3 text-uppercase">Транспорт</h5>
                        <label>
                            <input name="vehicle_id" placeholder="Введите id" class="form-control" value="" required />
                        </label><br />
                        <button class="btn btn-danger mt-3">Удалить</button>
                    </form>
                </div>
            </div>
            <div class="col card bg-dark text-white mt-5 mx-5" style="border-radius: 1rem;">
                <div class="card-body p-5 text-center">
                    <form action="delete_auto_part.py" method="POST">
                        <h5 class="fw-bold mb-3 text-uppercase">Комплектующие</h5>
                        <label>
                            <input name="auto_part_id" placeholder="Введите id" class="form-control" value="" required />
                        </label><br />
                        <button class="btn btn-danger mt-3">Удалить</button>
                    </form>
                </div>
            </div>
        </div>
        
        <div class="row">
            <div class="col card bg-dark text-white mt-5 mx-5" style="border-radius: 1rem;">
                <div class="card-body p-5 text-center">
                    <form action="add_user.py" method="POST">
                        <h5 class="fw-bold mb-3 text-uppercase">Пользователи</h5>
                        <label class="mb-3">
                            <input name="first_name" placeholder="Введите имя" class="form-control" value="" required />
                        </label><br />
                        <label class="mb-3">
                            <input name="last_name" placeholder="Введите фамилию" class="form-control" value="" required />
                        </label><br />
                        <label class="mb-3">
                            <input name="login" placeholder="Введите логин" class="form-control" value="" required />
                        </label><br />
                        <label class="mb-3">
                            <input name="pass_hash" placeholder="Введите хэш пароля" class="form-control" value="" required />
                        </label><br />
                        <button class="btn btn-success">Добавить</button>
                    </form>
                </div>
            </div>
            <div class="col card bg-dark text-white mt-5 mx-5" style="border-radius: 1rem;">
                <div class="card-body p-5 text-center">
                    <form action="add_vehicle.py" method="POST">
                        <h5 class="fw-bold mb-3 text-uppercase">Транспорт</h5>
                        <label class="mb-3">
                            <input name="brand" placeholder="Введите бренд" class="form-control" value="" required />
                        </label><br />
                        <label class="mb-3">
                            <input name="model" placeholder="Введите модель" class="form-control" value="" required />
                        </label><br />
                        <label class="mb-3">
                            <input name="year" placeholder="Введите год" class="form-control" value="" required />
                        </label><br />
                        <label class="mb-3">
                            <input name="price" placeholder="Введите цену" class="form-control" value="" required />
                        </label><br />
                        <label class="mb-3">
                            <input name="owner_id" placeholder="Введите id владельца" class="form-control" value="" required />
                        </label><br />
                        <button class="btn btn-success">Добавить</button>
                    </form>
                </div>
            </div>
            <div class="col card bg-dark text-white mt-5 mx-5" style="border-radius: 1rem;">
                <div class="card-body p-5 text-center">
                    <form action="add_auto_part.py" method="POST">
                        <h5 class="fw-bold mb-3 text-uppercase">Комплектующие</h5>
                        <label class="mb-3">
                            <input name="manufacturer" placeholder="Введите производителя" class="form-control" value="" required />
                        </label><br />
                        <label class="mb-3">
                            <input name="name" placeholder="Введите название" class="form-control" value="" required />
                        </label><br />
                        <label class="mb-3">
                            <input name="price" placeholder="Введите цену" class="form-control" value="" required />
                        </label><br />
                        <label class="mb-3">
                            <input name="seller_id" placeholder="Введите id продавца" class="form-control" value="" required />
                        </label><br />
                        <button class="btn btn-success">Добавить</button>
                    </form>
                </div>
            </div>
        </div>
        
        <div class="container bg-dark text-white mt-4">
            <p class="fs-3 fw-bold mb-0">Пользователи</p>
        </div>
        <div class="table-responsive">
            <table class="table table-dark table-striped table-bordered">
                <thead>
                    <th>id</th>
                    <th>Имя</th>
                    <th>Фамилия</th>
                    <th>Логин</th>
                    <th>Хэш пароля</th>
                </thead>
                <tbody>""")
c.execute("SELECT rowid, * FROM users")
users = c.fetchall()
for user in users:
    print(f"<tr>"
          f"<td>{user[0]}</td>"
          f"<td>{user[1]}</td>"
          f"<td>{user[2]}</td>"
          f"<td>{user[3]}</td>"
          f"<td>{user[4]}</td>"
          f"</tr>")
print("""       </tbody>
            </table>
        </div>
        <div class="container bg-dark text-white mt-3">
            <p class="fs-3 fw-bold mb-0">Транспорт</p>
        </div>
        <div class="table-responsive">
            <table class="table table-dark table-striped table-bordered">
                <thead>
                    <th>id</th>
                    <th>Бренд</th>
                    <th>Модель</th>
                    <th>Год</th>
                    <th>Цена</th>
                    <th>id владельца</th>
                </thead>
                <tbody>""")
c.execute("SELECT rowid, * FROM vehicles")
vehicles = c.fetchall()
for v in vehicles:
    print(f"<tr>"
          f"<td>{v[0]}</td>"
          f"<td>{v[1]}</td>"
          f"<td>{v[2]}</td>"
          f"<td>{v[3]}</td>"
          f"<td>{v[4]}</td>"
          f"<td>{v[5]}</td>"
          f"</tr>")
print("""       </tbody>
            </table>
        </div>
        <div class="container bg-dark text-white mt-3">
            <p class="fs-3 fw-bold mb-0">Комплектующие</p>
        </div>
        <div class="table-responsive mb-3">
            <table class="table table-dark table-striped table-bordered">
                <thead>
                    <th>id</th>
                    <th>Производитель</th>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>id продавца</th>
                </thead>
                <tbody>""")
c.execute("SELECT rowid, * FROM auto_parts")
auto_parts = c.fetchall()
for ap in auto_parts:
    print(f"<tr>"
          f"<td>{ap[0]}</td>"
          f"<td>{ap[1]}</td>"
          f"<td>{ap[2]}</td>"
          f"<td>{ap[3]}</td>"
          f"<td>{ap[4]}</td>"
          f"</tr>")
print("""       </tbody>
            </table>
        </div>
    </div>

    <footer class="bg-dark text-white p-5 mt-auto">
        <div>© Luxury Autos 2024</div>
    </footer>
</body>

</html>""")

db.close()