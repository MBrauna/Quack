<!DOCTYPE html>
<html>
    <head>
        <!-- Zona para tratamento dinâmico do título -->
        <title>{{ config('app.name', 'Quack!') }}</title>
        <!-- Zona para tratamento dinâmico do título -->

        <!-- CSRF Token -->
        <meta name="csrf-token" content="{{ csrf_token() }}">
        <!-- CSRF Token -->

        <!-- Favicon -->
        <link rel="apple-touch-icon" sizes="57x57" href="icone/apple-icon-57x57.png">
        <link rel="apple-touch-icon" sizes="60x60" href="icone/apple-icon-60x60.png">
        <link rel="apple-touch-icon" sizes="72x72" href="icone/apple-icon-72x72.png">
        <link rel="apple-touch-icon" sizes="76x76" href="icone/apple-icon-76x76.png">
        <link rel="apple-touch-icon" sizes="114x114" href="icone/apple-icon-114x114.png">
        <link rel="apple-touch-icon" sizes="120x120" href="icone/apple-icon-120x120.png">
        <link rel="apple-touch-icon" sizes="144x144" href="icone/apple-icon-144x144.png">
        <link rel="apple-touch-icon" sizes="152x152" href="icone/apple-icon-152x152.png">
        <link rel="apple-touch-icon" sizes="180x180" href="icone/apple-icon-180x180.png">
        <link rel="icon" type="image/png" sizes="192x192"  href="icone/android-icon-192x192.png">
        <link rel="icon" type="image/png" sizes="32x32" href="icone/favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="96x96" href="icone/favicon-96x96.png">
        <link rel="icon" type="image/png" sizes="16x16" href="icone/favicon-16x16.png">
        <link rel="manifest" href="icone/manifest.json">
        <meta name="msapplication-TileColor" content="#6a00bc">
        <meta name="msapplication-TileImage" content="icone/ms-icon-144x144.png">
        <meta name="theme-color" content="#6a00bc">
        <!-- Favicon -->

        <!-- Configurações da página -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Configurações da página -->

        <!-- Configurações para as descrições site -->
        <meta name="author"   content="MBrauna - Quack!">
        <meta name="keywords" content="Inteligência artificial, roteirização, mapa, detecção facial, Rede neural, deep learning, machine learning">
        <!-- Configurações para as descrições site -->

        <!-- Para Icones -->
        <link rel="stylesheet" type="text/css" href="Quack/Quack/assets/vendor/font-awesome/css/font-awesome.min.css">
        <link rel="stylesheet" type="text/css" href="Quack/Quack/assets/vendor/linearicons/style.css">
        <!-- Para Icones -->

        <!-- Para Frameworks -->
        <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,600,700">
        <!-- Para frameworks -->

        <!-- CSS dinâmico -->
        @yield('css_dinamico')
        <!-- CSS dinâmico -->

        <!-- JS fixo 
        <script type="text/javascript" src="Quack/quack.js"></script>
        - JS fixo -->

        <!-- JS dinâmico -->
        @yield('js_dinamico')
        <!-- JS dinâmico -->
    </head>
    <body class="quack-site" id="topo">
        <div id="wrapper">
            <header class="menu">
                @yield('menu')
            </header>

            <div class="main">
                <div class="main-content">
                    <div class="container-fluid">
                        <!-- Corpo dinâmico -->
                        @yield('corpo')
                        <!-- Corpo dinâmico -->
                    </div>
                </div>
            </div>

            <footer>
                <div class="container-fluid">
                    <p class="copyright">&copy; 2019 - Quack! Tecnologia</p>
                </div>
            </footer>

        </div> <!-- <div id="wrapper"> -->

        <!-- Scripts de rodapé -->
        @yield('script')
        <!-- Scripts de rodapé -->
    </body> <!-- <body class="quack-site" id="topo"> -->
</html>