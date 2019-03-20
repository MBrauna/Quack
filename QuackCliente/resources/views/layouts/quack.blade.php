<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport"   content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- CSRF Token -->
        <meta name="csrf-token" content="{{ csrf_token() }}">
    
        <!-- Carregamento dos ícarones -->
        <link rel="apple-touch-icon" sizes="76x76" href="favicon.ico">
        <link rel="icon" type="image/png" href="favicon.ico">
        <link href="./Quack/css/nucleo-icons.css" rel="stylesheet" />

        <!-- Para fontes -->
        <link href="https://fonts.googleapis.com/css?family=Poppins:200,300,400,600,700,800" rel="stylesheet" />
        <link href="https://use.fontawesome.com/releases/v5.0.6/css/all.css" rel="stylesheet">

        <!-- Para título -->
        <title>{{ config('app.name', 'Laravel') }}</title>


        <!-- CSS Files -->
        <link href="./Quack/css/blk-design-system.css?v=1.0.0" rel="stylesheet" />
        <link href="./Quack/quack/quack.css" rel="stylesheet" />


        <!-- CSS Dinâmico -->
        @yield('css_dinamico')
        <!-- CSS DInâmico -->
    </head>
    <!-- Início do corpo Quack - Preenchimento dinâmico -->
    <body class="index-page">

        <!-- Barra principal - Topo -->
        <nav class="navbar navbar-expand-lg fixed-top navbar-transparent " color-on-scroll="100">
            <div class="container">
                <div class="navbar-translate">
                    <a class="navbar-brand" href="{{ url('/') }}" rel="tooltip" title="Pensou novo? Quack!" data-placement="bottom" target="_blank">
                        <span>Quack •</span> Tecnologia
                    </a>
                    <button class="navbar-toggler navbar-toggler" type="button" data-toggle="collapse" data-target="#navigation" aria-controls="navigation-index" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-bar bar1"></span>
                        <span class="navbar-toggler-bar bar2"></span>
                        <span class="navbar-toggler-bar bar3"></span>
                    </button>
                </div>
                <div class="collapse navbar-collapse justify-content-end" id="navigation">
                    <div class="navbar-collapse-header">
                        <div class="row">
                            <div class="col-6 collapse-brand">
                                <a>Quack</a>
                            </div>
                            <div class="col-6 collapse-close text-right">
                                <button type="button" class="navbar-toggler" data-toggle="collapse" data-target="#navigation" aria-controls="navigation-index" aria-expanded="false" aria-label="Toggle navigation">
                                    <i class="tim-icons icon-simple-remove"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                    <ul class="navbar-nav">
                        <li class="nav-item p-0">
                            <a class="nav-link" rel="tooltip" title="Oi @, bora?!" data-placement="bottom" href="https://twitter.com/CreativeTim" target="_blank">
                                <i class="fab fa-twitter"></i>
                                <p class="d-lg-none d-xl-none">Twitter</p>
                            </a>
                        </li>
                        <li class="nav-item p-0">
                            <a class="nav-link" rel="tooltip" title="Deixa seu like ai!" data-placement="bottom" href="https://www.facebook.com/CreativeTim" target="_blank">
                                <i class="fab fa-facebook-square"></i>
                                <p class="d-lg-none d-xl-none">Facebook</p>
                            </a>
                        </li>
                        <li class="nav-item p-0">
                            <a class="nav-link" rel="tooltip" title="E lá vamos nós pros insta!" data-placement="bottom" href="https://www.instagram.com/CreativeTimOfficial" target="_blank">
                                <i class="fab fa-instagram"></i>
                                <p class="d-lg-none d-xl-none">Instagram</p>
                            </a>
                        </li>
                        <li class="dropdown nav-item">
                            <a href="#" class="dropdown-toggle nav-link" data-toggle="dropdown">
                                <i class="fa fa-cogs d-lg-none d-xl-none"></i>Comece agora!
                            </a>
                            @if (Route::has('login'))
                                <div class="dropdown-menu dropdown-with-icons">
                                @auth
                                    <a class="dropdown-item" href="{{ url('/painel') }}">Painel de controle</a>
                                @else
                                    <a class="dropdown-item" href="{{ route('login') }}">Acessar</a>

                                    @if (Route::has('register'))
                                    <a class="dropdown-item" href="{{ route('register') }}">Cadastrar</a>
                                    @endif
                                @endauth
                                </div>
                            @endif
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <!-- Barra principal - Topo -->


        <!-- Para conteúdo -->
        <div class="wrapper">
            <!-- Conteúdo principal -->
            <div class="page-header header-filter">
                <div class="squares square1"></div>
                <div class="squares square2"></div>
                <div class="squares square3"></div>
                <div class="squares square4"></div>
                <div class="squares square5"></div>
                <div class="squares square6"></div>
                <div class="squares square7"></div>
                <div class="container">
                    @yield('conteudo_principal')
                </div>
            </div> <!-- <div class="page-header header-filter"> -->
            <!-- Conteúdo principal -->
            
            <div class="main">
                @yield('conteudo')
            </div> <!-- <div class="main"> -->
        </div>
        <!-- Para conteúdo -->


        <!-- ROdapé -->
        <footer class="footer">
            <div class="container">
                <div class="row">
                    <div class="col-md-3">
                        <h1 class="title">Quack</h1>
                    </div>
                    <div class="col-md-3">
                        <ul class="nav">
                            <li class="nav-item">
                                <a href="{{ url('/') }}" class="nav-link">
                                    Principal
                                </a>
                            </li>
                            <li class="nav-item">
                                <a href="{{ route('login') }}" class="nav-link">
                                    Painel administrativo
                                </a>
                            </li>
                            <li class="nav-item">
                                <a href="{{ route('register') }}" class="nav-link">
                                    Registrar
                                </a>
                            </li>
                            <li class="nav-item">
                                <a href="{{ route('login') }}" class="nav-link">
                                    Perfil
                                </a>
                            </li>
                        </ul>
                    </div>
                    <div class="col-md-3">
                        <ul class="nav">
                            <li class="nav-item">
                                <a href="{{ route('login') }}" class="nav-link">
                                    Contato
                                </a>
                            </li>
                            <li class="nav-item">
                                <a href="{{ route('login') }}" class="nav-link">
                                    Sobre nós
                                </a>
                            </li>
                            <li class="nav-item">
                                <a href="{{ route('login') }}" class="nav-link">
                                    QuackBlog
                                </a>
                            </li>
                            <li class="nav-item">
                                <a href="{{ route('login') }}" class="nav-link">
                                    Termos de uso
                                </a>
                            </li>
                        </ul>
                    </div>
                    <div class="col-md-3">
                        <h3 class="title">Supreenda-se</h3>
                        <div class="btn-wrapper profile">
                            <a target="_blank" href="https://twitter.com/" class="btn btn-icon btn-neutral btn-round btn-simple" data-toggle="tooltip" data-original-title="Oi @! Estamos aqui.">
                                <i class="fab fa-twitter"></i>
                            </a>
                            <a target="_blank" href="https://www.facebook.com/" class="btn btn-icon btn-neutral btn-round btn-simple" data-toggle="tooltip" data-original-title="Deixa seu like!">
                                <i class="fab fa-facebook-square"></i>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
        <!-- ROdapé -->



        <!-- Para Scripts -->
        @yield('scripts')
        <!-- Para Scripts -->
    </body>
    <!-- Início do corpo Quack - Preenchimento dinâmico -->
</html>