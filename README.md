<hr>
<h1>Trabajo Práctico 3</h1>
<h2>Introducción</h2>
<p>El objetivo de este trabajo práctico es el de modelar Internet: las páginas web y sus interacciones.
Nos interesa modelar cómo podemos navegar a través de Internet. Se quiere poder realizarse varias
consultas para poder entender distintos aspectos de la red. Se trabajará con porciones
ínfimas de la red.</p>
<h2>Datos disponibles</h2>
<p>Vamos a trabajar con una ínfima porción de Internet, del portal llamado &quot;Wikipedia&quot;. Es posible descargarse el contenido completo de Wikipedia en cualquier idioma desde <a href="https://dumps.wikimedia.org/backup-index.html">aquí</a>. Nosotros nos enfocaremos en la versión en español, si bien el trabajo es completamente compatible con cualquier otro idioma, hay idiomas con mucha mas carga que otros.</p>
<p>Además, les brindamos a ustedes <a href="https://drive.google.com/file/d/0B_oxuLrlET2hMmx3N0dGR2dNMWc/view?usp=sharing">un parser implementado en Python</a> para que no sea necesario que ustedes lo implementen. En caso de preferir implementar algún cambio sobre el mismo, o utilizar uno propio, no hay inconvenientes. Igualmente, para que no sea necesario consumir tiempo en esta tarea se brinda <a href="https://drive.google.com/file/d/1JOxK7E0bqW3yfuj3niGpPOaWCX7vo_8Q/view?usp=sharing">un archivo de texto de salida ya parseado</a>, que una vez descomprimido pesa 1.3GB. Dicho archivo proviene del dump de Wikipedia en español hasta el día 1/5/2016, pero ya es posible descargar versiones más actualizadas, o bien de otras wikis.
En caso de no utilizar ese archivo, o simplemente para experimentar (con otro idioma, por ejemplo) pueden simplemente ejecutarlo haciendo:</p>
<pre><code>    $ python wiki_parser.py &lt;path_dump&gt; &lt;path_parsed&gt;
</code></pre>
<p>El archivo parseado tiene el formato TSV (cada campo es separado por un tab):</p>
<pre><code>TituloArticulo1 Link1   Link2   Link3   ... LinkN
TituloArticulo2 Link1   Link2   Link3   ... LinkM
...
</code></pre>
<p>Dichos links deben hacer referencia a otros Títulos de Artículos. Tener en cuenta que, por simpleza del parser, pueden haber links que referencien a artículos que no existan. Por ejemplo: se han filtrado las entradas de artículos referentes a años para hacer más liviano el archivo y más interesantes los caminos a recorrer por nuestra &quot;Pequeña Internet&quot;.</p>
<p>Considerar que el archivo completo cuenta con más de 3 millones de artículos. Por lo tanto, para que puedan también realizar pruebas más rápidas, les brindamos un archivo de <a href="https://drive.google.com/file/d/1b0fZPVE2e1z4TGFL9n4ZiqAnEMAU25rs/view?usp=sharing">una reducción de la primera red</a> que cuenta con los primeros 75.000 artículos visitados resultantes al realizar un recorrido BFS desde 'Argentina' en el set de datos completo de Wikipedia.</p>
<h2>Consigna</h2>
<p>Dado este archivo parseado, se debe modelar Internet con una estructura Grafo considerando únicamente los títulos de las páginas y las conexiones entre ellas. Esto implica determinar todas las características necesarias para el grafo.
Se pide implementar un programa que cargue inicialmente el grafo recibiendo como parámetro la ruta del archivo parseado:</p>
<pre><code>    $ ./netstats wiki-reducido-75000.tsv
</code></pre>
<p>Una vez cargada la red, se deberán realizar acciones sobre la misma a partir de comandos ingresados desde entrada estándar.</p>
<h3>Implementación</h3>
<p>El trabajo puede realizarse en lenguaje a elección, siendo aceptados Python y C, y cualquier otro a ser discutido con el corrector asignado.</p>
<p>El trabajo consiste de 3 partes:</p>
<ol>
<li>El TDA Grafo, con sus primitivas completamente agnósticas sobre su uso para modelar la red de Internet.</li>
<li>Una biblioteca de funciones de grafos, que permitan hacer distintas operaciones sobre un grafo que modela Internet, sin importar cuál es la red específica.</li>
<li>El programa <code>NetStats</code> que utilice tanto el TDA como la biblioteca para poder implementar todo
lo requerido.</li>
</ol>
<p>Es importante notar que las primeras dos partes deberían poder funcionar en cualquier contexto: El TDA Grafo para cualquier tipo de TP3 (o utilidad); la biblioteca de funciones debe funcionar para aplicar cualquiera de las funciones implementadas sobre cualquier grafo que tenga las características de las de este TP (particularmente, dirigido y no pesado). La tercera parte es la que se encuentra enteramente acoplada al TP en particular.</p>
<p>El programa debe recibir por parámetro, cargar en memoria el set de datos (<code>$ ./netstats wiki-reducido-75000.tsv</code>) y luego solicitar el ingreso de comandos por entrada estándar,
del estilo <code>&lt;comando&gt; 'parametro'</code>. Notar que esto permite tener un archivo de instrucciones a ser
ejecutadas (i.e. <code>$ ./netstats wiki-reducido-75000.tsv &lt; entrada.txt</code>).</p>
<p>De todas las funcionalidades, pueden optar por implementar distintas. Algunas consideraciones:</p>
<ol>
<li>Cada funcionalidad e implementación otorga distinta cantidad de puntos, basado en dificultad y
el interés del curso en que implementen dicha funcionalidad o implementación
particular de la misma (Cada estrella ★ corresponde a un punto).</li>
<li>Se deben conseguir al menos 10 puntos para poder aprobar el TP.</li>
<li>En caso de obtener menos de 12 puntos, la nota máxima será 9.</li>
<li>En caso de obtener 16 puntos o más la nota máxima del trabajo práctico puede llegar a 11.</li>
<li>El total de puntos entre todas las funcionalidades es 18.</li>
</ol>
<p>A continuación se listarán los comandos junto a ejemplos de entrada y salidas para el caso de la red reducida.
Recomendamos trabajar con este set de datos, puesto que el original cuenta con una enorme cantidad de datos, por lo que
puede demorar mucho tiempo cada una de las pruebas a realizar.</p>
<h4>Listar operaciones (obligatorio, sin puntos)</h4>
<ul>
<li>Comando: <code>listar_operaciones</code>.</li>
<li>Parámetros: ninguno.</li>
<li>Utilidad: Dado que no todas las funcionalidades o implementaciones son obligatorias, debe
existir un comando que nos permita saber cuáles son las funcionalidades disponibles. Debe
imprimirse una línea por cada <strong>comando</strong> que esté implementado.</li>
<li>Complejidad: Este comando debe ejecutar en <img src="https://i.upmath.me/svg/%5Cmathcal%7BO%7D(1)" alt="\mathcal{O}(1)" />.</li>
<li>Ejemplo:
Entrada:<pre><code>listar_operaciones
</code></pre>
</li>
</ul>
<p>Salida:
<code>camino mas_importantes conectados ciclo en_rango</code></p>
<h4>Camino más corto (★)</h4>
<ul>
<li>Comando: <code>camino</code>.</li>
<li>Parámetros: <code>origen</code> y <code>destino</code>. Origen y destino son <strong>páginas</strong>.</li>
<li>Utilidad: nos imprime una lista con las <strong>páginas</strong> con los cuales navegamos de la página <code>origen</code> a la página <code>destino</code>, navegando lo menos posible.</li>
<li>Complejidad: Este comando debe ejecutar en <img src="https://i.upmath.me/svg/%5Cmathcal%7BO%7D(P%20%2B%20L)" alt="\mathcal{O}(P + L)" />, siendo <img src="https://i.upmath.me/svg/P" alt="P" /> la cantidad
de páginas, y <img src="https://i.upmath.me/svg/L" alt="L" /> la cantidad de Links en toda la red.</li>
<li>Ejemplos:
Entrada:<pre><code>camino Argentina,Zinedine Zidane
camino Jeremy Irons,pejerrey
camino handball,Napoleón Bonaparte
</code></pre>
</li>
</ul>
<p>Salida:
<code>Argentina -&gt; Francia -&gt; Zinedine Zidane Costo: 2 Jeremy Irons -&gt; Reino Unido -&gt; Patagonia argentina -&gt; Río Grande (Tierra del Fuego) -&gt; pejerrey Costo: 4 No se encontro recorrido</code></p>
<h4>Artículos más importantes (★★★)</h4>
<p>Utlizaremos el algoritmo de <a href="/algo2/material/apuntes/pagerank">PageRank</a> para implementar este comando,
dado que además fue pensado primordialmente para este escenario.</p>
<ul>
<li>Comando: <code>mas_importantes</code>.</li>
<li>Parámetros: <code>n</code>, la cantidad de páginas más importantes a mostrar.</li>
<li>Utilidad: nos muestra las <code>n</code> páginas más centrales/importantes del mundo según el algoritmo de
pagerank, ordenadas de mayor importancia a menor importancia.</li>
<li>Complejidad: Este comando debe ejecutar en <img src="https://i.upmath.me/svg/%5Cmathcal%7BO%7D(K(P%20%2B%20L)%20%2B%20P%20%5Clog%20(n))" alt="\mathcal{O}(K(P + L) + P \log (n))" />, siendo <img src="https://i.upmath.me/svg/K" alt="K" /> la cantidad de
iteraciones a realizar para llegar a la convergencia (puede simplificarse a <img src="https://i.upmath.me/svg/%5Cmathcal%7BO%7D(P%20%5Clog%20n%20%2B%20L)" alt="\mathcal{O}(P \log n + L)" />
(El término <img src="https://i.upmath.me/svg/%5Cmathcal%7BO%7D(P%20%5Clog%20n)" alt="\mathcal{O}(P \log n)" /> proviene de obtener los Top-n luego de haber aplicado el algoritmo).</li>
<li>Ejemplo:
Entrada:<pre><code>mas_importantes 20
</code></pre>
</li>
</ul>
<p>Salida:
<code>Argentina, Estados Unidos, Buenos Aires, España, Francia, Provincias de la Argentina, Magnoliophyta, Alemania, México, Reino Unido, Europa, Italia, Brasil, Chile, Perú, Segunda Guerra Mundial, Uruguay, Inglaterra, Venezuela, Colombia</code></p>
<p><strong>Importante</strong>: Considerar que esto podría pedirse varias veces por ejecución, y no se desea repetir el calculo (ya que no debería el valor de pagerank de cada artículo).</p>
<h4>Conectividad (★★)</h4>
<ul>
<li>Comando: <code>conectados</code>.</li>
<li>Parámetros: <code>página</code>, la página que se le quiere obtener la conectividad.</li>
<li>Utilidad: nos muestra todos las páginas a los que podemos llegar desde la <code>página</code> pasado por parámetro y que, a su vez, puedan también volver a dicha <code>página</code>.</li>
<li>Complejidad: Este comando debe ejecutar en <img src="https://i.upmath.me/svg/%5Cmathcal%7BO%7D(P%20%2B%20L)" alt="\mathcal{O}(P + L)" />. Considerar que a todas las páginas a las que lleguemos también se conectan entre sí, y con el tamaño del set de datos puede convenir guardar los resultados.</li>
<li>Ejemplo:
Entrada:<pre><code>conectados Boca Juniors
conectados Argentina
</code></pre>
</li>
</ul>
<p>Salida: En ambos casos la CFC está compuesta por los mismos artículos. Dejamos acá <a href="https://drive.google.com/file/d/1bRfZa4vLlN6olhrcPNHEt-FYvWGFNbuI/view?usp=sharing">un archivo con la salida esperada</a> (no necesariamente en ese orden, pero sí <em>esos</em> artículos), dado que la misma consta de 43569 de los 75000 artículos. Es importante notar que la segunda consulta debería obtener un resultado en tiempo constante.</p>
<h4>Ciclo de n artículos (★★★)</h4>
<ul>
<li>Comando: <code>ciclo</code>.</li>
<li>Parámetros: <code>página</code> y <code>n</code>.</li>
<li>Utilidad: permite obtener un ciclo de largo <code>n</code> que comience en la página indicada.</li>
<li>Complejidad: Este comando debe ejecutar en <img src="https://i.upmath.me/svg/%5Cmathcal%7BO%7D(P%5En)" alt="\mathcal{O}(P^n)" />, pero realizando una buena poda puede reducirse
sustancialmente el tiempo de ejecución.</li>
<li>Ejemplo:
Entrada:<pre><code>ciclo Jeremy Irons,4
ciclo Polonia,20
</code></pre>
</li>
</ul>
<p>Salida:
<code>Jeremy Irons -&gt; The Silence of the Lambs (película) -&gt; Dances with Wolves -&gt; Premios Óscar Polonia -&gt; Unión Europea Occidental -&gt; Unión Europea -&gt; Idioma italiano -&gt; Florencia -&gt; Cannes -&gt; Festival de Cannes -&gt; Biarritz -&gt; Pirineos Atlánticos -&gt; Pirineos -&gt; Alpes -&gt; Dolomitas -&gt; Marmolada -&gt; Italia -&gt; Pier Paolo Pasolini -&gt; Roma -&gt; Alfabeto fonético internacional -&gt; Alfabeto Fonético Internacional -&gt; Idioma ruso -&gt; Moscú</code></p>
<h4>Lectura a las 2 a.m. (★★)</h4>
<ul>
<li>Comando: <code>lectura</code>.</li>
<li>Parámetros: <code>página1</code>, <code>página2</code>, …, <code>página_n</code>.</li>
<li>Utilidad: Permite obtener un orden en el que es válido leer las páginas indicados. Para que un orden sea válido, si <code>página_i</code> tiene un link a <code>página_j</code>, entonces es necesario <strong>primero leer</strong> <code>página_j</code>. Solo se debe tener en cuenta los artículos mencionados en los parámetros. Esto, por supuesto, puede implicar que no podamos cumplir con lo pedido por encontrarnos con un ciclo.</li>
<li>Complejidad: Este comando debe ejecutar en <img src="https://i.upmath.me/svg/%5Cmathcal%7BO%7D(n%20%2B%20L_n)" alt="\mathcal{O}(n + L_n)" />, siendo <img src="https://i.upmath.me/svg/n" alt="n" /> la cantidad de páginas indicadas, y <img src="https://i.upmath.me/svg/L_n" alt="L_n" /> la cantidad de links entre estas.</li>
<li>Ejemplo:
Entrada:<pre><code>lectura Buenos Aires,Roma
lectura Hockey sobre hielo,Roma,Japón,árbol,Guerra,Dios,universo,Himalaya,otoño
</code></pre>
</li>
</ul>
<p>Salida:
<code>No existe forma de leer las paginas en orden otoño, Himalaya, universo, Dios, Guerra, árbol, Hockey sobre hielo, Japón, Roma</code></p>
<p><strong>Importante</strong>: considerar lo indicado en el enunciado. Si quiero saber un orden válido para leer <code>página1</code> y <code>página2</code>, y hay un link de <code>página1</code> a <code>página2</code>, un orden válido es <code>página2</code> y luego <code>página1</code>.</p>
<h4>Diametro (★)</h4>
<ul>
<li>Comando: <code>diametro</code>.</li>
<li>Parámetros: ninguno.</li>
<li>Utilidad: permite obtener el diámetro de toda la red. Esto es, obtener el camino mínimo más grande de toda la red. <em>Nota</em>: Puede haber más de uno de estos, pero todos tendrán el mismo largo.</li>
<li>Complejidad: Este comando debe ejecutar en <img src="https://i.upmath.me/svg/%5Cmathcal%7BO%7D(P(P%20%2B%20L))" alt="\mathcal{O}(P(P + L))" />.</li>
<li>Ejemplo: Debido a la complejidad, aplicar sobre el grafo incluso reducido puede demorar muchas horas. Por lo tanto, les acercamos <a href="https://drive.google.com/file/d/1aQXpMFlALkujRj74_bOdl18OtIR_8QBZ/view?usp=sharing">un ejemplo con 5.000 artículos</a>.
Entrada:<pre><code>diametro
</code></pre>
</li>
</ul>
<p>Salida:
<code>Huésped (biología) -&gt; Agente biológico patógeno -&gt; Animalia -&gt; Carlos Linneo -&gt; Finlandia -&gt; Unión Europea -&gt; Robert Schuman -&gt; Aristide Briand Costo: 7</code></p>
<h4>Todos en Rango (★)</h4>
<ul>
<li>Comando: <code>rango</code>.</li>
<li>Parámetros: <code>página</code> y <code>n</code>.</li>
<li>Utilidad: permite obtener la cantidad de páginas que se encuenten a <strong>exactamente</strong> <code>n</code> links/saltos desde la <code>página</code> pasada por parámetro.</li>
<li>Complejidad: Este comando debe ejecutar en <img src="https://i.upmath.me/svg/%5Cmathcal%7BO%7D(P%20%2B%20L)" alt="\mathcal{O}(P + L)" />.</li>
<li>Ejemplo:
Entrada:<pre><code>rango Tokio,8
rango Tokio,3
rango Perón,4
</code></pre>
</li>
</ul>
<p>Salida:
<code>0 39360 53385</code></p>
<h4>Comunidades (★★)</h4>
<ul>
<li>Comando: <code>comunidad</code>.</li>
<li>Parámetros: <code>página</code>.</li>
<li>Utilidad: permite obtener la comunidad dentro de la red a la que pertenezca la página pasada por parámetro. Para esto, utilizaremos el sencillo algoritmo de <a href="/algo2/material/apuntes/label_propagation">Label Propagation</a>.</li>
<li>Ejemplo:
Entrada:<pre><code>comunidad Chile
</code></pre>
</li>
</ul>
<p>Salida: Dado que la salida puede ser muy grande <a href="https://drive.google.com/file/d/1LoDZhGYDdE0LkKN_QMM9Vo1hOZbvqm_y/view?usp=sharing">adjuntamos una salida de ejemplo</a>. No es requisito que la salida sea tal cual está (ni en orden ni los artículos), y se tendrá consideración las diferencias que se puedan llegar a tener. La idea de implementar este comando es que tengan un primer acercamiento a un algoritmo muy sencillo para detectar comunidades. En este caso, pueden ver que muchas páginas relacionadas a Chile y ciudades de Chile han quedado en la misma comunidad, lo cual sería un resultado esperable.</p>
<p>A quién le interese este tema puede ver otro tipo de algoritmos, como por ejemplo el <a href="https://es.wikipedia.org/wiki/M%C3%A9todo_de_Louvain">Algoritmo de Louvain</a>.</p>
<h4>Navegacion por primer link (★)</h4>
<ul>
<li>Comando: <code>navegación</code>.</li>
<li>Parámetros: <code>origen</code>.</li>
<li>Utilidad: Se dice que si comenzamos en <em>cualquier</em> artículo de wikipedia, y navegamos únicamente utilizando el primer link, eventualmente llegaremos al artículo de <em>Filosofía</em>. Por lo tanto, queremos implementar un comando que navegue usando el primer link (de los que tengamos reportados) desde la página <code>origen</code> y navegando usando siempre el primer link. Debemos continuar accediendo al primer link hasta que la página ya no tenga links, o bien hasta que hayamos llegado a 20 páginas.</li>
<li>Complejidad: este comando debe ejecutar en <img src="https://i.upmath.me/svg/%5Cmathcal%7BO%7D(n)" alt="\mathcal{O}(n)" />.</li>
<li>Ejemplo:
Entrada:<pre><code>navegacion Argentina
navegacion Alemania
navegacion queso
navegacion Bolivia
navegacion Brasil
</code></pre>
</li>
</ul>
<p>Salida:
<code>Argentina -&gt; polacos Alemania -&gt; Derecho penal -&gt; complicidad queso Bolivia -&gt; Guerra del Acre -&gt; Hevea brasiliensis -&gt; Guerra del Acre -&gt; Hevea brasiliensis -&gt; Guerra del Acre -&gt; Hevea brasiliensis -&gt; Guerra del Acre -&gt; Hevea brasiliensis -&gt; Guerra del Acre -&gt; Hevea brasiliensis -&gt; Guerra del Acre -&gt; Hevea brasiliensis -&gt; Guerra del Acre -&gt; Hevea brasiliensis -&gt; Guerra del Acre -&gt; Hevea brasiliensis -&gt; Guerra del Acre -&gt; Hevea brasiliensis -&gt; Guerra del Acre -&gt; Hevea brasiliensis Brasil -&gt; Hermeto Pascoal -&gt; Portugués brasileño -&gt; caña de azúcar</code></p>
<h4>Coeficiente de Clustering (★★)</h4>
<p>El <a href="https://en.wikipedia.org/wiki/Clustering_coefficient"><em>Coeficiente de Clustering</em></a> es una métrica que nos permite entender cuán agrupados se encuentran los vértices de un grafo. Para explicarla de manera simplificada, es similar a plantear la proporción en la que se cumple al regla de transitividad: <em>Cuántos de mis adyacentes son adyacentes entre sí</em>.</p>
<p>El coeficiente de clustering de un vértice <img src="https://i.upmath.me/svg/i" alt="i" /> en un grafo dirigido puede calcularse como:</p>
<p align="center"><img align="center" src="https://i.upmath.me/svg/%20C_i%20%3D%20%5Cfrac%7B%5Cleft%7Ce_%7Bij%7D%3A%20v_j%2C%20v_k%20%5Cin%20%5Ctext%7Badyacentes%7D(v_i)%2C%20e_%7Bij%7D%20%5Cin%20%5Cmathcal%7BE%7D%20%5Cright%7C%7D%7Bk_i(k_i%20-%201)%7D%20" alt=" C_i = \frac{\left|e_{ij}: v_j, v_k \in \text{adyacentes}(v_i), e_{ij} \in \mathcal{E} \right|}{k_i(k_i - 1)} " /></p>
<p>Lo cual quiere decir: por cada par de adyacentes al vértice en cuestión, si existe la arista yendo de uno al otro (si además está la recíproca, lo contamos otra vez). A esa cantidad de aristas lo dividimos por <img src="https://i.upmath.me/svg/k_i(k_i%20-%201)" alt="k_i(k_i - 1)" /> siendo <img src="https://i.upmath.me/svg/k_i" alt="k_i" /> el grado de salida del vértice <img src="https://i.upmath.me/svg/i" alt="i" />. En caso de tener menos de 2 adyacentes, se define que el coeficiente de clustering de dicho vértice es 0. Considerar que el coeficiente de clustering es siempre un número entre 0 y 1.</p>
<p>El clustering promedio de toda la red será:</p>
<p align="center"><img align="center" src="https://i.upmath.me/svg/%20C%20%3D%20%5Cfrac%7B1%7D%7Bn%7D%20%5Csum_%7B%5Cforall%20v%20%5Cin%20%5Ctext%7Bgrafo%7D%7D%20C_i%20" alt=" C = \frac{1}{n} \sum_{\forall v \in \text{grafo}} C_i " /></p>
<ul>
<li>Comando: <code>clustering</code></li>
<li>Parámetros: <code>pagina</code>, opcional.</li>
<li>Utilidad: Permite obtener el coeficiente de clustering de la página indicada. En caso de no indicar página, se deberá informar el clustering promedio de la red. En ambos casos, informar con hasta 3 dígitos decimales.</li>
<li>Complejidad: En caso que se indique una página en particular, debe ejecutar en <img src="https://i.upmath.me/svg/%20~%20%5Cmathcal%7BO%7D(1)%20" alt=" ~ \mathcal{O}(1) " /> (considerando que la red es <em>muy</em> dispersa). En caso que no se indique ninguna página, deberá ejecutar en <img src="https://i.upmath.me/svg/%20%5Cmathcal%7BO%7D((P%20%2B%20L)%5E2)%20" alt=" \mathcal{O}((P + L)^2) " />.</li>
<li>Ejemplo:
Entrada:<pre><code>clustering River Plate
clustering Club Atlético River Plate
clustering Juan Domingo Perón
clustering Ámsterdam
# Ejemplo con la red de 5.000 artículos:
clustering
</code></pre>
</li>
</ul>
<p>Salida:
<code>0.000 0.030 0.020 0.065 # Ejemplo con la red de 5.000 artículos: 0.122</code></p>
<h2>Entrega</h2>
<p>Adicionalmente a los archivos propios del trabajo práctico debe agregarse un archivo <code>entrega.mk</code> que contenga la regla <code>netstats</code> para generar el ejecutable de dicho programa (sea compilando o los comandos que fueren necesarios). Por ejemplo, teniendo un TP elaborado en Python, podría ser:</p>
<pre><code class="language-makefile">netstats: netstats.py grafo.py biblioteca.py
    cp netstats.py netstats
    chmod +x netstats
</code></pre>
<p><strong>Importante</strong>: En caso de recibir un error <code>FileNotFoundError: [Errno 2] No such file or directory: './netstats': './netstats'</code>, tener en cuenta que para el caso de enviar código escrito en Python es necesario además indicar la ruta del intérprete. Esto puede hacerse agregando como primera línea del archivo principal (en el ejemplo, sería <code>netstats.py</code>) la línea: <code>#!/usr/bin/python3</code>.</p>
<h2>Criterios de aprobación</h2>
<p>El código entregado debe ser claro y legible y ajustarse a las especificaciones
de la consigna. Debe compilar sin advertencias y correr sin errores de memoria.</p>
<p>La entrega incluye, obligatoriamente, los siguientes archivos de código:</p>
<ul>
<li>el código del TDA Grafo programado, y cualquier otro TDA que fuere necesario.</li>
<li>el código de la solución del TP.</li>
</ul>
<p>La entrega se realiza en forma digital a través del <a href="%7B%7Bsite.entregas%7D%7D">sistema de entregas</a>,
con todos los archivos mencionados en un único archivo ZI</p>
