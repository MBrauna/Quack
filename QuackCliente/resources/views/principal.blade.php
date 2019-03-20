@extends('layouts.quack')




@section('css_dinamico')
<link rel="stylesheet" type="text/css" href="Letras/css/normalize.css" />
<link rel="stylesheet" type="text/css" href="Letras/css/quackletra.css" />
<link rel="stylesheet" type="text/css" href="Letras/css/playful.css" />
@endsection













@section('conteudo_principal')
<section class="content content--layout">
    <h2 class="word word--playful">Quack</h2>
</section>
@endsection


@section('conteudo')

@endsection








@section('scripts')
<svg class="hidden">
    <symbol id="icon-arrow" viewBox="0 0 24 24">
        <title>arrow</title>
        <polygon points="6.3,12.8 20.9,12.8 20.9,11.2 6.3,11.2 10.2,7.2 9,6 3.1,12 9,18 10.2,16.8 "/>
    </symbol>
    <symbol id="icon-drop" viewBox="0 0 24 24">
        <title>drop</title>
        <path d="M12,21c-3.6,0-6.6-3-6.6-6.6C5.4,11,10.8,4,11.4,3.2C11.6,3.1,11.8,3,12,3s0.4,0.1,0.6,0.3c0.6,0.8,6.1,7.8,6.1,11.2C18.6,18.1,15.6,21,12,21zM12,4.8c-1.8,2.4-5.2,7.4-5.2,9.6c0,2.9,2.3,5.2,5.2,5.2s5.2-2.3,5.2-5.2C17.2,12.2,13.8,7.3,12,4.8z"/><path d="M12,18.2c-0.4,0-0.7-0.3-0.7-0.7s0.3-0.7,0.7-0.7c1.3,0,2.4-1.1,2.4-2.4c0-0.4,0.3-0.7,0.7-0.7c0.4,0,0.7,0.3,0.7,0.7C15.8,16.5,14.1,18.2,12,18.2z"/>
    </symbol>
    <symbol id="icon-github" viewBox="0 0 32.6 31.8">
        <title>github</title>
        <path d="M16.3,0C7.3,0,0,7.3,0,16.3c0,7.2,4.7,13.3,11.1,15.5c0.8,0.1,1.1-0.4,1.1-0.8c0-0.4,0-1.4,0-2.8c-4.5,1-5.5-2.2-5.5-2.2c-0.7-1.9-1.8-2.4-1.8-2.4c-1.5-1,0.1-1,0.1-1c1.6,0.1,2.5,1.7,2.5,1.7c1.5,2.5,3.8,1.8,4.7,1.4c0.1-1.1,0.6-1.8,1-2.2c-3.6-0.4-7.4-1.8-7.4-8.1c0-1.8,0.6-3.2,1.7-4.4C7.4,10.7,6.8,9,7.7,6.8c0,0,1.4-0.4,4.5,1.7c1.3-0.4,2.7-0.5,4.1-0.5c1.4,0,2.8,0.2,4.1,0.5c3.1-2.1,4.5-1.7,4.5-1.7c0.9,2.2,0.3,3.9,0.2,4.3c1,1.1,1.7,2.6,1.7,4.4c0,6.3-3.8,7.6-7.4,8c0.6,0.5,1.1,1.5,1.1,3c0,2.2,0,3.9,0,4.5c0,0.4,0.3,0.9,1.1,0.8c6.5-2.2,11.1-8.3,11.1-15.5C32.6,7.3,25.3,0,16.3,0z"/>
    </symbol>
</svg>
<!-- JavaScript Core -->
<script src="./Quack/js/core/jquery.min.js"                         type="text/javascript"></script>
<script src="./Quack/js/core/popper.min.js"                         type="text/javascript"></script>
<script src="./Quack/js/core/bootstrap.min.js"                      type="text/javascript"></script>
<script src="./Quack/js/plugins/perfect-scrollbar.jquery.min.js"    type="text/javascript"></script>

<!--  Plugin for Switches, full documentation here: http://www.jque.re/plugins/version3/bootstrap.switch/ -->
<script src="./Quack/js/plugins/bootstrap-switch.js"                type="text/javascript"></script>

<!--  Plugin for the Sliders, full documentation here: http://refreshless.com/nouislider/ -->
<script src="./Quack/js/plugins/nouislider.min.js"                  type="text/javascript"></script>

<!-- Chart JS -->
<script src="./Quack/js/plugins/chartjs.min.js"                     type="text/javascript"></script>

<!--  Plugin for the DatePicker, full documentation here: https://github.com/uxsolutions/bootstrap-datepicker -->
<script src="./Quack/js/plugins/moment.min.js"                      type="text/javascript"></script>
<script src="./Quack/js/plugins/bootstrap-datetimepicker.js"        type="text/javascript"></script>

<!-- Black Dashboard DEMO methods, don't include it in your project! -->
<script src="./Quack/quack/quack.js"                                type="text/javascript"></script>

<!-- Control Center for Black UI Kit: parallax effects, scripts for the example pages etc -->
<script src="./Quack/js/blk-design-system.min.js?v=1.0.0"           type="text/javascript"></script>
<script>
    $(document).ready(function()
    {
        blackKit.initDatePicker();
        blackKit.initSliders();
    });

    function scrollToDownload()
    {
        if ($('.section-download').length != 0)
        {
            $("html, body").animate(
            {
                scrollTop: $('.section-download').offset().top
            }, 1000);
        }
    }
</script>
<script src="Letras/js/charming.min.js"></script>
<script src="Letras/js/anime.min.js"></script>
<script src="Letras/js/letra.js"></script>
<script src="Letras/js/letra5.js"></script>
@endsection