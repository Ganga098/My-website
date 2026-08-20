<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
        }

        header {
            background-color: #333;
            color: white;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin: 15px;
        }

        section {
            padding: 50px;
        }

        .box {
            background-color: white;
            padding: 30px;
            margin: 20px auto;
            max-width: 600px;
            border-radius: 10px;
        }

        footer {
            background-color: #333;
            color: white;
            padding: 15px;
        }
    </style>
</head>

<body>

    <header>
        <h1>My Simple Website</h1>

        <nav>
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#contact">Contact</a>
        </nav>
    </header>

    <section id="home">
        <div class="box">
            <h2>Welcome!</h2>
            <p>This is my simple static website hosted using GitHub Pages.</p>
        </div>
    </section>

    <section id="about">
        <div class="box">
            <h2>About Us</h2>
            <p>We create simple and user-friendly websites using HTML and CSS.</p>
        </div>
    </section>

    <section id="contact">
        <div class="box">
            <h2>Contact</h2>
            <p>Email: example@gmail.com</p>
        </div>
    </section>

    <footer>
        <p>© 2026 My Website</p>
    </footer>

</body>
</html>
