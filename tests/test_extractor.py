"""Test class Extractor."""

from os import chdir, getcwd, remove
from os.path import getmtime, isfile
from pytest import fixture

from opentaal import Extractor

# pylint:disable=missing-function-docstring,redefined-outer-name


@fixture
def extractor():
    return Extractor()


@fixture
def extractor_override():
    return Extractor(override=True)


@fixture
def tmp_path() -> str:
    path = 'tmp_extractor.html'
    original = getcwd()
    if getcwd().endswith('/tests'):
        chdir('..')
    with open(path, 'w') as file:
        file.write("""<!doctype html>
<html lang="en" prefix="og: http://ogp.me/ns#">
<head>
<script defer="" async="" src="https://stats.intergalactic.fm/matomo.js"></script>
<script>var _paq = _paq || [];(function(){var u=(("https:" == document.location.protocol) ? "https://stats.intergalactic.fm/" : "http://stats.intergalactic.fm/");_paq.push(["setSiteId", "1"]);_paq.push(["setTrackerUrl", u+"matomo.php"]);_paq.push(["setDoNotTrack", 1]);_paq.push(["setCookieDomain", ".intergalactic.fm"]);if (!window.matomo_search_results_active) {_paq.push(["trackPageView"]);}_paq.push(["setIgnoreClasses", ["no-tracking","colorbox"]]);_paq.push(["enableLinkTracking"]);var d=document,g=d.createElement("script"),s=d.getElementsByTagName("script")[0];g.type="text/javascript";g.defer=true;g.async=true;g.src=u+"matomo.js";s.parentNode.insertBefore(g,s);})();</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="og:updated_time" property="og:updated_time" content="1715159895">
<meta name="og:site_name" property="og:site_name" content="Intergalactic FM Festival 2024">
<meta name="og:title" property="og:title" content="Intergalactic FM Festival 2024">
<meta name="og:type" property="og:type" content="website">
<meta name="og:image" property="og:image" content="https://intergalactic.fm/festival/2024/ifm-fest-2024-5000x2617.png">
<meta name="og:image:width" property="og:image:width" content="5000">
<meta name="og:image:height" property="og:image:height" content="2617">
<meta name="og:url" property="og:url" content="https://intergalactic.fm/festival/2024/">
<meta name="og:description" property="og:description" content="May 9 - 12, The Hague. Mad DJ and live action.">
<link rel="icon" href="favicon.ico" type="image/vnd.microsoft.icon">
<title>Intergalactic FM Festival 2024</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="">
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
<style>
@font-face {
font-family: "broadway-bt";
    src: url("broadway-bt.woff") format('woff');
}
h1, h2 {
    font-family: broadway-bt, monospace;
}
body {
    text-align: center;
    background-color: #4a266a;
    color: #f18c00;
    font-family: monospace, monospace;
}
a:link, a:visited, a:active, a:hover {
    color: #f18c00;
}
#mapidPRC {
    width: 300px;
    height: 300px;
}
</style>
<body>
<h1>INTERGALACTIC FM FESTIVAL 2024</h1>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
May&nbsp;9&nbsp;-&nbsp;12,  The&nbsp;Hague, the&nbsp;Netherlands
<img style="width:100%;" src="ifm-fest-2024-8000x4500.png" alt="Intergalactic FM Festival 2024 flyer with building in portrait">
<small>Updated Wed 08 May 2024, 11:05 CET</small>
<br>
<br>
<h2><a id="schedule">SCHEDULE</a></h2>
<div class="container text-center"><div class="row align-items-start">
<div class="col">
    Thursday&nbsp;May&nbsp;9, 16:00&nbsp;-&nbsp;00:00
    <br>
    donation-based entrance, PRC
    <br>&nbsp;
</div>
<div class="col">
    Friday&nbsp;May&nbsp;10, 18:00&nbsp;-&nbsp;05:00
    <br>
    ticket required, PRC&nbsp;+&nbsp;PIP
    <br>&nbsp;
</div>
</div></div>

<div class="container text-center"><div class="row align-items-start">
<div class="col">
    Saturday&nbsp;May&nbsp;11, 18:00&nbsp;-&nbsp;06:00
    <br>
    ticket required, PRC&nbsp;+&nbsp;PIP
    <br>&nbsp;
</div>
<div class="col">
    Sunday&nbsp;May&nbsp;12, 18:00&nbsp;-&nbsp;01:00
    <br>
    ticket required, PRC
    <br>&nbsp;
</div>
</div></div>
<h2><a id="tickets">TICKETS</a></h2>
Get your tickets for
<br>
<br>
<div class="container text-center"><div class="row align-items-start">
<div class="col">
    <a target="_blank" href="https://pip.stager.co/web/tickets/111310037">Friday €&nbsp;25.00</a>
    <br>
    <a target="_blank" href="https://pip.stager.co/web/tickets/111310040">Saturday €&nbsp;25.00</a>
    <br>&nbsp;
</div>
<div class="col">
    <a target="_blank" href="https://pip.stager.co/web/tickets/111399150">Fri&nbsp;+&nbsp;Sat €&nbsp;42.50</a>
    <br>
    <a target="_blank" href="https://pip.stager.co/web/tickets/111310042">Sunday €&nbsp;10.00</a>
    <br>&nbsp;
</div>
</div></div>
<h2><a id="lineup">LINEUP</a></h2>
Mad DJ and live action
<br>
<br>
<div class="container text-center"><div class="row align-items-start">
<div class="col">
030303
<br>
AFRA
<br>
ALESSANDRO&nbsp;ADRIANI&nbsp;(LIVE)
<br>
ALESSANDRO&nbsp;PARISI
<br>
AROY&nbsp;DEE
<br>
BAZ&nbsp;REZNIK
<br>
BENJI&nbsp;DF
<br>
BETONKUST&nbsp;(LIVE)
<br>
BEVERLY&nbsp;HILLS&nbsp;808303
<br>
BOG
<br>
CHARLIE&nbsp;(LIVE)
<br>
COSMIC&nbsp;FORCE&nbsp;(LIVE)
<br>
DAS&nbsp;DING&nbsp;(LIVE)
<br>
DAVID&nbsp;SPANISH
<br>
DAVID&nbsp;VUNK
<br>
DECIPHER
<br>
DECKARD
<br>
DIMGARDEN
<br>
DJ&nbsp;OVERDOSE
<br>
DRMR
<br>
DYNAMIC&nbsp;D
<br>
EDGAR&nbsp;NEVERMOO
<br>
EKMAN&nbsp;(LIVE)
<br>
ELECTRONOME
<br>
ELEKTORTEK&nbsp;(LIVE)
<br>
ENDFEST
<br>
ENKA
<br>
ESTHER&nbsp;DUNE
<br>
FERRE&nbsp;DE&nbsp;RIDDER
<br>
FILMMAKER
<br>
GAMMA&nbsp;INTEL
<br>
GARÇON&nbsp;TAUPE
</div>
<div class="col">
GRASS&nbsp;HARP
<br>
IAN&nbsp;MARTIN
<br>
INTERGALACTIC&nbsp;GARY
<br>
INTERNAL&nbsp;OPERATOR
<br>
INVOLUCIJA&nbsp;FT. FIUME&nbsp;(LIVE)
<br>
I-F
<br>
JANNAH
<br>
KAFKACTRL
<br>
KENNEDY
<br>
KLANKMAN
<br>
KORBEN&nbsp;BALAS
<br>
L.F.T.
<br>
LAZERCAT
<br>
LE&nbsp;CHOCOLAT&nbsp;NOIR
<br>
LEGOWELT
<br>
LORADENIZ
<br>
LOUD-E
<br>
LUCA&nbsp;DELL'ORSO
<br>
MACCHINA&nbsp;NERA
<br>
MARK&nbsp;DU&nbsp;MOSCH
<br>
MARSMAN
<br>
MAX&nbsp;SINCLAIR
<br>
MENSCHMASCHINE
<br>
MIQKAEL
<br>
MONO-POLY&nbsp;(LIVE)
<br>
MOOT
<br>
MULE&nbsp;DRIVER&nbsp;(LIVE)
<br>
NAKS
<br>
NIELS&nbsp;KLEIN
<br>
NOWY
<br>
OFRA
<br>
ORGUE&nbsp;ELECTRONIQUE&nbsp;FT. FRE2K&nbsp;(LIVE)
</div>
<div class="col">
PAUL&nbsp;DU&nbsp;LAC
<br>
PAWEL&nbsp;BLOT
<br>
PRIVACY
<br>
QUEEN&nbsp;SABA
<br>
RADIATION&nbsp;30376
<br>
RICHELLE&nbsp;SOIGNI
<br>
ROBERT&nbsp;BERGMAN
<br>
ROBERTO&nbsp;AUSER
<br>
ROBOTIC&nbsp;AF
<br>
RON&nbsp;MORELLI
<br>
SEJA
<br>
SELENE
<br>
SERGE
<br>
SHARLESE
<br>
SLICKCHICK
<br>
SNUFFO&nbsp;(LIVE)
<br>
STAATSEINDE&nbsp;(LIVE)
<br>
STARBOROUGH
<br>
STEVIE&nbsp;KOTEY
<br>
STELKON
<br>
SWISS ARROW&nbsp;(LIVE)
<br>
SYNCOM&nbsp;DATA
<br>
SYROB
<br>
TLR
<br>
VASCO
<br>
VERGAARBAK
<br>
VINCENT&nbsp;KNOL
<br>
VIOLET&nbsp;POISON&nbsp;(LIVE)
<br>
VOLPEVOLPE
<br>
WERA
<br>
WRONG&nbsp;SAL
<br>
YASH
<br>
ZONZO
</div>
</div></div>
<!--TO BE ANNOUNCED IN
<br>
<div id="countdowntimer"></div>
<script>
var countDownDate = new Date("Apr 12, 2024 14:00:00").getTime();
var x = setInterval(function() {
  var now = new Date().getTime();
  var distance = countDownDate - now;
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
  document.getElementById("countdowntimer").innerHTML = days + " days, " + hours + " hours, "
  + minutes + " minutes, " + seconds + " seconds ";
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("countdowntimer").innerHTML = "EXPIRED";
  }
}, 1000);
</script-->
<br>
<h2><a id="location">LOCATION</a></h2>
Panama Racing Club (PRC) and <a target="_blank" href="https://pipdenhaag.nl/">PIP Den Haag</a> are located at Binckhorstlaan 36 (BINK36), The Hague, the Netherlands. Both only accept payments by debit card.
<br>
<br>
The location is a 15 minute walk from the train stations Den Haag Centraal or Den Haag HS (Holland Spoor). Bicycles can be rented out and a taxi might require waiting half an hour at peak times.
<br>
<br>
Food stalls and lockers are available at the festival. On Sunday, ZAHARA Cocktailbar will be mixing your favorite drinks. For your safety and style, do not wear flipflops to the festival.
<br>
<br>
<div id="mapidPRC" class="center center-block" style="width:100%; margin:0 auto;"></div>
<script>
    var mapPRC = L.map('mapidPRC', {attributionControl: false}).setView([52.0735573, 4.3332564], 17);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}&optimize=true', {
      maxZoom: 20, minZoom: 12, attribution: 'OSM',
      id: 'mapbox/dark-v10', tileSize: 512, zoomOffset: -1
    }).addTo(mapPRC);
    var redIcon = new L.Icon({
      iconUrl: 'marker-ifm-64.png',
      iconRetinaUrl: 'marker-ifm-128.png',
      iconSize: [64, 64],
      iconAnchor: [32, 32]
    });
    var marker = L.marker([52.0735573, 4.3332564], {icon: redIcon}).addTo(mapPRC);
</script>
<br>
<h2><a id="accommodation">ACCOMMODATION</a></h2>
Note that accommodation is in high demand this particular weekend.
<br>
<br>
<h2><a id="promotion">PROMOTION</a></h2>
Our promotional images to share are
<br>
<br>
<div class="container text-center"><div class="row align-items-start">
<div class="col">
    <a href="ifm-fest-2024-5000x2617.png">banner&nbsp;landscape</a>
    <br>
    <a href="ifm-fest-2024-4500x8000.png">banner&nbsp;portrait</a>
    <br>&nbsp;
</div>
<div class="col">
    <a href="ifm-fest-2024-building-4501x4501.png">building&nbsp;square</a>
    <br>
    <a href="ifm-fest-2024-building-4501x5625.png">building&nbsp;portrait</a>
    <br>&nbsp;
</div>
<div class="col">
    <a href="ifm-fest-2024-train-4501x4501.png">train&nbsp;square</a>
    <br>
    <a href="ifm-fest-2024-train-4500x5625.png">train&nbsp;portrait</a>
    <br>&nbsp;
</div>
</div></div>
Our promotional videos to share are
<br>
<br>
<div class="container text-center"><div class="row align-items-start">
<div class="col">
    <a href="ifm-fest-2024-lineup-1080x1080.mp4">promo&nbsp;square</a>
    <br>&nbsp;
</div>
<div class="col">
    <a href="ifm-fest-2024-lineup-1080x1920.mp4">promo&nbsp;portrait</a>
    <br>&nbsp;
</div>
<div class="col">
    <a href="ifm-fest-2024-lineup-1920x1080.mp4">promo&nbsp;landscape</a>
    <br>&nbsp;
</div>
</div></div>
<h2><a id="stuff">STUFF</a></h2>
Let us spend your money with
<br>
<br>
<div class="container text-center"><div class="row align-items-start">
<div class="col">
    <a target="_blank" href="https://intergalactic.fm/shop">IFMX&nbsp;Shop</a>
    <br>&nbsp;
</div>
<div class="col">
    <a target="_blank" href="https://www.paypal.com/donate/?hosted_button_id=MV4HVU2D4W3LJ">Donate&nbsp;to&nbsp;IFM</a>
    <br>&nbsp;
</div>
<div class="col">
    <a target="_blank" href="https://viewlexx.bandcamp.com/">Bandcamp</a>
    <br>&nbsp;
</div>
</div></div>
<h2><a id="media">MEDIA</a></h2>
Like, share and comment on
<br>
<br>
<div class="container text-center"><div class="row align-items-start">
<div class="col">
    <a target="_blank" href="https://www.instagram.com/intergalacticfm">Insta&nbsp;@intergalacticfm</a>
    <br>
    <a target="_blank" href="https://www.instagram.com/explore/tags/intergalacticfm/">Insta&nbsp;#intergalacticfm</a>
    <br>
    <a target="_blank" href="https://www.instagram.com/pipdenhaag">Insta&nbsp;@pipdenhaag</a>
    <br>
    <a target="_blank" href="https://ra.co/events/1886555">Resident Advisor</a>
    <br>&nbsp;
</div>
<div class="col">
    <a target="_blank" href="https://www.facebook.com/events/1522400338329244/">Fbook Thursday</a>
    <br>
    <a target="_blank" href="https://www.facebook.com/events/928869052110868/">Fbook Friday</a>
    <br>
    <a target="_blank" href="https://www.facebook.com/events/719773933361146/">Fbook Saturday</a>
    <br>
    <a target="_blank" href="https://www.facebook.com/events/317936257703962/">Fbook Sunday</a>
    <br>&nbsp;
</div>
<div class="col">
    <a target="_blank" href="https://partyflock.nl/event/intergalactic-fm-festival-nl">Partyflock</a>
    <br>
    <a target="_blank" href="https://www.youtube.com/@IntergalacticFMX">YouTube</a>
    <br>
    <a target="_blank" href="https://odysee.com/@intergalacticfm:0">Odysee</a>
    <br>
    <a target="_blank" href="https://archive.org/details/@intergalacticfm">Internet&nbsp;Archive</a>
    <br>&nbsp;
</div>
</div></div>
<h2><a id="support">SUPPORT</a></h2>
The festival has been brought to you with the support of
<br>
<br>
<div class="container text-center"><div class="row align-items-start">
<div class="col">
    Stichting&nbsp;Hotmix
    <br>
    <a target="_blank" href="https://denhaag.nl">City&nbsp;of&nbsp;The&nbsp;Hague</a>
    <br>&nbsp;
</div>
<div class="col">
    Panama Racing Club
    <br>
    <a target="_blank" href="https://zaharacocktailbar.nl/">ZAHARA&nbsp;Cocktailbar</a>
    <br>&nbsp;
</div>
<div class="col">
    <a target="_blank" href="https://pipdenhaag.nl/">PIP&nbsp;Den&nbsp;Haag</a>
    <br>
    <a target="_blank" href="https://www.instagram.com/reveal.utrecht">REVEAL&nbsp;Utrecht</a>
    <br>&nbsp;
</div>
</div></div>
<a target="_blank" href="https://intergalactic.fm/newsletter/signup">Subscribe to the IFMX&nbsp;Newsletter</a>
<br>
<br>
<small>© 2024 Intergalactic FM™</small>
</body>
</html>""")
    chdir(original)

    return path


def test_extractor(extractor, tmp_path: str):
    original = getcwd()
    if getcwd().endswith('/tests'):
        chdir('..')
    out = f'{tmp_path[:-4]}txt'
    assert extractor.extract(tmp_path)
    assert isfile(out)
    first = getmtime(out)
    assert not extractor.extract(tmp_path)
    assert isfile(out)
    assert getmtime(out) == first
    remove(out)
    chdir(original)


def test_extractor_override(extractor_override, tmp_path):
    original = getcwd()
    if getcwd().endswith('/tests'):
        chdir('..')
    out = f'{tmp_path[:-4]}txt'
    assert extractor_override.extract(tmp_path)
    assert isfile(out)
    first = getmtime(out)
    assert extractor_override.extract(tmp_path)
    assert isfile(out)
    assert getmtime(out) != first
    remove(out)
    chdir(original)
