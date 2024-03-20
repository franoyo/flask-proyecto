from flask import Flask, render_template, request,  redirect, url_for, flash, session
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'crudflask'

app.secret_key = 'mysecretkey'
mysql=MySQL(app)
@app.route('/')
def index():
    return render_template('landinPage.html')
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Obtiene los datos del formulario
        username = request.form['username']
        password = request.form['password']
        
        # Verifica si el usuario ya existe en la base de datos
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM alumno WHERE nombre = %s", (username,))
        user = cur.fetchone()
        if user:
            cur.close()
            flash('El nombre de usuario ya está en uso. Por favor, elija otro.', 'error')
        else:
            # Si el usuario no existe, inserta el nuevo usuario en la base de datos
            cur.execute("INSERT INTO alumno (nombre, password) VALUES (%s, %s)", (username, password))
            mysql.connection.commit()
            cur.close()
            flash('El usuario ha sido craeado correctamente', 'success')
            return redirect(url_for('login'))
    
    # Si la solicitud es GET, muestra el formulario de login
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtiene los datos del formulario
        username = request.form['correo']
        password = request.form['contraseña']
        
        # Verifica si las credenciales son válidas
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM alumno WHERE nombre = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()

        # Si el usuario existe, inicia sesión y redirige a la página principal
        if user:
            session['loggedin'] = True
            session['username'] = username
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('crud'))
        else:
            # Si las credenciales son incorrectas, muestra un mensaje de error
            flash('Credenciales incorrectas. Inténtalo de nuevo.', 'error')

    # Si la solicitud es GET o si las credenciales son incorrectas, muestra el formulario de inicio de sesión
    return render_template('login.html')

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    # Elimina todas las variables de sesión
    session.clear()
    flash('Cierre de sesión exitoso.', 'success')
    return redirect(url_for('login'))

# Ruta para la página principal (requiere inicio de sesión)


@app.route('/crud')
def crud():
    # Verifica si el usuario ha iniciado sesión
    if 'loggedin' in session:
        # Si ha iniciado sesión, realiza la consulta a la base de datos y renderiza la plantilla
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM curso')
        data = cur.fetchall()
        cur.close()
        return render_template('index.html', cursos=data)
    else:
        # Si no ha iniciado sesión, muestra un mensaje flash y redirige al usuario a la página de inicio de sesión
        flash('Por favor, inicia sesión para acceder a esta página.', 'error')
        return redirect(url_for('login'))

@app.route('/add_cursos', methods=['GET','POST'])
def add_cursos():
    if 'loggedin' in session:
        if request.method == "POST":
            codigo=request.form['codigo']
            nombre=request.form['nombre']
            horas=request.form['horas']
            area=request.form['area']
            cur=mysql.connection.cursor()
            cur.execute('INSERT INTO curso (codigo,nombre,horas,area) VALUES(%s, %s, %s, %s)',(codigo,nombre,horas,area)) 
            mysql.connection.commit()
            flash('El curso ha sido agregado correctamente', 'success')
            return redirect(url_for('crud'))
        else:
            return render_template('index.html')
    else:
        flash('Por favor, inicia sesión para acceder a esta página.', 'error')
        return redirect(url_for('login'))
@app.route('/delete', methods=['POST'])  # Asegúrate de permitir solo solicitudes POST
def delete():
    id = request.form['id']
    cur = mysql.connection.cursor()
    sql = "DELETE FROM curso WHERE ID = %s"
    cur.execute(sql, (id,))
    mysql.connection.commit()
    flash('El curso ha sido eliminado correctamente', 'success')
    return redirect(url_for('crud'))
@app.route('/edit/<int:id>')
def get_curso(id):
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM curso WHERE id = %s', (id,))
        data = cur.fetchall() # Retorna un único valor
        return render_template('editarCrud.html', c=data[0])
@app.route('/update/<id>', methods=['POST'])
def update_curso(id):
    
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        horas = request.form['horas']
        area = request.form['area']
        cur = mysql.connection.cursor()
        cur.execute('UPDATE curso SET codigo = %s, nombre = %s, horas = %s, area = %s WHERE id = %s' ,(codigo,nombre,horas,area,id))
        mysql.connection.commit()
        flash('El curso ha sido actualizado correctamente!', 'success')
    return redirect(url_for('crud'))

       

