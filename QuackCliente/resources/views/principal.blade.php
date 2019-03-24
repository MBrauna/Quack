@extends('layouts.quack')




@section('css_dinamico')
<link rel="stylesheet" type="text/css" href="Letras/css/normalize.css" />
<link rel="stylesheet" type="text/css" href="Letras/css/quackletra.css" />
<link rel="stylesheet" type="text/css" href="Letras/css/playful.css" />
@endsection













@section('conteudo_principal')
<section class="content content--layout">
    <h2 class="word word--playful">Quack</h2>
    <p class="center">Pensou novo? Quack</p>
</section>
@endsection












@section('conteudo')
<div class="section section-tabs">
    <div class="container">
        <div class="row">
            <div class="col-md-10 ml-auto col-xl-10 mr-auto">
                <div class="card">
                    <div class="card-header">
                        <ul class="nav nav-tabs nav-tabs-primary" role="tablist">
                            <li class="nav-item">
                                <a class="nav-link active" data-toggle="tab" href="#link1" role="tablist">
                                    <i class="tim-icons icon-spaceship"></i> Detecção
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" data-toggle="tab" href="#link2" role="tablist">
                                    <i class="tim-icons icon-settings-gear-63"></i> Predição
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" data-toggle="tab" href="#link3" role="tablist">
                                    <i class="tim-icons icon-bag-16"></i> Options
                                </a>
                            </li>
                        </ul>
                    </div>
                    <div class="card-body">
                        <div class="tab-content tab-space">
                            <div class="tab-pane active" id="link1">
                                <p>
                                    Collaboratively administrate empowered markets via plug-and-play networks. Dynamically   procrastinate B2C users after installed base benefits.
                                    <br />
                                    <br/>
                                    Dramatically visualize customer directed convergence without revolutionary ROI.
                                </p>
                            </div>
                            <div class="tab-pane" id="link2">
                                <p>
                                    Completely synergize resource taxing relationships via premier niche markets. Professionally cultivate one-to-one customer service with robust ideas.
                                    <br />
                                    <br/>
                                    Dynamically innovate resource-leveling customer service for state of the art customer service.
                                </p>
                            </div>
                            <div class="tab-pane" id="link3">
                                <p>
                                    Efficiently unleash cross-media information without cross-media value. Quickly maximize timely deliverables for real-time schemas.
                                    <br />
                                    <br/>
                                    Dramatically maintain clicks-and-mortar solutions without functional solutions.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection








@section('scripts')

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
<script src="./Quack/js/blk-design-system.js?v=1.0.0"               type="text/javascript"></script>
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