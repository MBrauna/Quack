<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport"   content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- CSRF Token -->
        <meta name="csrf-token" content="{{ csrf_token() }}">
        <!-- CSRF Token -->

        <!-- Para título -->
        <title>{{ config('app.name', 'Quack!') }}</title>
        <!-- Para título -->
    
        <!-- Tipos de icones -->
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">
        <!-- Tipos de icones -->

        <!-- Para fontes -->
        <link href="https://fonts.googleapis.com/css?family=Poppins:200,300,400,600,700,800" rel="stylesheet" />
        <link href="https://use.fontawesome.com/releases/v5.0.6/css/all.css" rel="stylesheet">
        <!-- Para fontes -->

        <!-- CSS Dinâmico -->
        @yield('css_dinamico')
        <!-- CSS DInâmico -->


        <!-- CSS/JS Arquivos fixos -->
        <link rel="stylesheet" type="text/css" href="Quack/Menu/css/default.css" />
        <link rel="stylesheet" type="text/css" href="Quack/Menu/css/component.css" />


        <script src="Quack/Menu/js/modernizr.custom.js"></script>
        <!-- CSS/JS Arquivos fixos -->
    </head>
    <body id="topo">
        <!-- Carregamento da carta de apresentação -->
        @yield('conteudo')
        <!-- Carregamento da carta de apresentação -->

        <div class="main clearfix">
            <nav id="menu" class="nav">
                    <ul>
                        <!-- Lista de menus disponíveis -->
                        @yield('menu')
                        <!-- Lista de menus disponíveis -->
                    </ul>
            </nav> <!-- <nav id="menu" class="nav"> -->
        </div> <!-- <div class="main clearfix"> -->

        <!-- Carrega os scripts dinamicamente -->
        @yield('scripts')
        <!-- Carrega os scripts dinamicamente -->

        <!-- Scripts Fixos -->
        <script>
            var changeClass = function (r,className1,className2)
            {
                var regex = new RegExp("(?:^|\\s+)" + className1 + "(?:\\s+|$)");
                if( regex.test(r.className) )
                {
                    r.className = r.className.replace(regex,' '+className2+' ');
                }
                else
                {
                    r.className = r.className.replace(new RegExp("(?:^|\\s+)" + className2 + "(?:\\s+|$)"),' '+className1+' ');
                }
                return r.className;
            };  

            var menuElements = document.getElementById('menu');
            menuElements.insertAdjacentHTML('afterBegin','<button type="button" id="menutoggle" class="navtoogle" aria-hidden="true"><i aria-hidden="true" class="icon-menu"> </i> Menu</button>');

            document.getElementById('menutoggle').onclick = function()
            {
                changeClass(this, 'navtoogle active', 'navtoogle');
            }

            document.onclick = function(e)
            {
                var mobileButton = document.getElementById('menutoggle'), buttonStyle =  mobileButton.currentStyle ? mobileButton.currentStyle.display : getComputedStyle(mobileButton, null).display;

                if(buttonStyle === 'block' && e.target !== mobileButton && new RegExp(' ' + 'active' + ' ').test(' ' + mobileButton.className + ' '))
                {
                    changeClass(mobileButton, 'navtoogle active', 'navtoogle');
                }
            }
        </script>
        <!-- Scripts FIxos -->
    </body>
</html>