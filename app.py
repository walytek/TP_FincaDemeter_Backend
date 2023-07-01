from flask import Flask
from flask import render_template 
from flask import request
from flaskext.mysql import MySQL

app=Flask(__name__,template_folder='template')
MySQL= MySQL()
app.config ['MYSQL_DATABASE_HOST']= 'Localhost'
app.config ['MYSQL_DATABASE_USER']= 'root'
app.config ['MYSQL_DATABASE_PASSWORD']= ''
app.config ['MYSQL_DATABASE_BD']= 'productos_demeter'
MySQL.init_app(app)
    
@app.route('/')
def home():
    return render_template('home.html')

        
 
@app.route('/productos')
def productos():
    sql= "SELECT * FROM productos_demeter.vinos;"
    conn = MySQL.connect()
    cursor = conn.cursor() 
    cursor.execute(sql) 
    productos = cursor.fetchall() 
    cursor.close()
    
    
    
    return render_template('productos.html',vinos=productos)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/store', methods=['POST'])
def storage():
    Ide=request.form['ID']
    Vinos=request.form['Tipo']
    Nombre=request.form['Producto']
    Valor=request.form['precio']
    Cantidad=request.form['stock']
    Fecha=request.form['Fecha']
    
    
    
    
    
    
    
    sql= "INSERT INTO `productos_demeter`.`vinos`(`Tipo de Vino`,`Producto`,`Precio`,`Stock`) VALUES ('"+Vinos +"', '"+Nombre +"',"+Valor +","+Cantidad +");" 
    conn = MySQL.connect()
    cursor = conn.cursor() 
    cursor.execute(sql) 
    
    conn.commit()
    
                                                                                                                                                                         
    return render_template('store.html')
    
@app.route('/delete/<Id>')
def delete(Id):
    
    
    sql = "DELETE FROM `productos_demeter`.`vinos` WHERE  Id= " + Id + ";" 
    conn = MySQL.connect()
    cursor = conn.cursor() 
    cursor.execute(sql) 
    conn.commit()
    
                                                                                                                                                                         
    return render_template('delete.html')

@app.route('/edit/<Id>')
def edit(Id):
    
    
        sql= " SELECT * FROM productos_demeter.vinos WHERE Id = " + Id + ";" 
        conn = MySQL.connect()
        cursor = conn.cursor() 
        cursor.execute(sql) 
        dataone_product= cursor.fetchone()
        conn.commit()

   
        return render_template('edit.html', jinja= dataone_product)

@app.route('/update', methods=['POST'])
def update():
    Ide=request.form['ID']
    Vinos=request.form['Tipo']
    Nombre=request.form['Producto']
    Valor=request.form['precio']
    Cantidad=request.form['stock']
    Fecha=request.form['Fecha']

    sql=" `productos_demeter`.`vinos` SET Tipo = '" + Vinos + "', Producto ='" + Nombre + "', precio = "+ Valor +",stock = "+ Cantidad  +",WHERE `Id` = "+ Ide +";"

    return render_template ('update.html')
 
if __name__=='__main__':
    app.run(debug=True) 
    
