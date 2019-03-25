@extends('layouts.quackintro')




@section('css_dinamico')
<link rel="stylesheet" type="text/css" href="Quack/Letras/css/normalize.css" />
<link rel="stylesheet" type="text/css" href="Quack/Letras/css/quackletra.css" />
<link rel="stylesheet" type="text/css" href="Quack/Letras/css/playful.css" />
@endsection





@section('menu')
                    <li>
                        <a href="#menu">
                            <span class="icon">
                                <i class="fab fa-asymmetrik"></i>
                            </span>
                            <span>Início</span>
                        </a>
                    </li>
                    <li>
                        <a href="#menu">
                            <span class="icon"> 
                                <i class="fas fa-chalkboard-teacher"></i>
                            </span>
                            <span>Experimente</span>
                        </a>
                    </li>
                    <li>
                        <a href="#menu">
                            <span class="icon">
                                <i class="fas fa-brain"></i>
                            </span>
                            <span>Serviços</span>
                        </a>
                    </li>
                    <li>
                        <a href="#menu">
                            <span class="icon">
                                <i class="fas fa-couch"></i>
                            </span>
                            <span>Blog</span>
                        </a>
                    </li>
                    <li>
                        <a href="#menu">
                            <span class="icon">
                                <i class="fas fa-street-view"></i>
                            </span>
                            <span>Quem somos</span>
                        </a>
                    </li>
                    <li>
                        <a href="#menu">
                            <span class="icon">
                                <i class="fas fa-at"></i>
                            </span>
                            <span>Contato</span>
                        </a>
                    </li>
@endsection





@section('conteudo')
    <section class="content content--layout">
        <h2 class="word word--playful">Quack!</h2>
    </section>
@endsection








@section('scripts')
<script src="Quack/Letras/js/charming.min.js"></script>
<script src="Quack/Letras/js/anime.min.js"></script>
<script src="Quack/Letras/js/letra.js"></script>
<script src="Quack/Letras/js/letra5.js"></script>
@endsection