from flaskblog import create_app # import library flaskblog, untuk menggunakan fungsi create app

app = create_app() # inisialisasi variable app

if __name__ == '__main__': # melakukan proses debug
    app.run(debug=True)
