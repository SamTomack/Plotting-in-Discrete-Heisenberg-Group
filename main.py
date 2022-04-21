<html>
<head>
<title>main.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6897bb;}
.s3 { color: #808080;}
.s4 { color: #6a8759;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
main.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">random</span>
<span class="s0">from </span><span class="s1">itertools </span><span class="s0">import </span><span class="s1">product</span>
<span class="s0">import </span><span class="s1">numpy </span><span class="s0">as </span><span class="s1">np</span>
<span class="s0">import </span><span class="s1">pyqtgraph </span><span class="s0">as </span><span class="s1">pg</span>
<span class="s0">import </span><span class="s1">pyqtgraph.opengl </span><span class="s0">as </span><span class="s1">gl</span>

<span class="s1">vectors = []</span>
<span class="s1">combSet = []</span>

<span class="s1">m = </span><span class="s2">7</span>

<span class="s3">#To use predetermined matrices</span>
<span class="s4">''' 
a0 = [1,0,-5] #[a,b,c] 
a1 = [2,-3,1] 
a2 = [8,-1,5] 
a3 = [-3,2,1] 
a4= [4,5,2] 
 
vectors.append(a0) 
vectors.append(a1) 
vectors.append(a2) 
vectors.append(a3) 
vectors.append(a4) 
'''</span>

<span class="s0">def </span><span class="s1">generateRandomMatrices(n):</span>
    <span class="s1">L = []</span>
    <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(</span><span class="s2">0</span><span class="s0">, </span><span class="s1">n):</span>
        <span class="s1">a = random.randrange(-</span><span class="s2">5</span><span class="s0">,</span><span class="s2">5</span><span class="s0">,</span><span class="s2">1</span><span class="s1">)</span>
        <span class="s1">b = random.randrange(-</span><span class="s2">5</span><span class="s0">,</span><span class="s2">5</span><span class="s0">,</span><span class="s2">1</span><span class="s1">)</span>
        <span class="s1">c = random.randrange(-</span><span class="s2">5</span><span class="s0">,</span><span class="s2">5</span><span class="s0">,</span><span class="s2">1</span><span class="s1">)</span>
        <span class="s1">L.append([a</span><span class="s0">,</span><span class="s1">b</span><span class="s0">,</span><span class="s1">c])</span>
    <span class="s0">return </span><span class="s1">L</span>

<span class="s1">vectors = generateRandomMatrices(</span><span class="s2">5</span><span class="s1">)</span>

<span class="s0">def </span><span class="s1">add(L1</span><span class="s0">, </span><span class="s1">L2): </span>
    <span class="s1">a = (L1[</span><span class="s2">0</span><span class="s1">] + L2[</span><span class="s2">0</span><span class="s1">])</span>
    <span class="s1">b = (L1[</span><span class="s2">1</span><span class="s1">] + L2[</span><span class="s2">1</span><span class="s1">])</span>
    <span class="s1">c = L1[</span><span class="s2">2</span><span class="s1">] + L2[</span><span class="s2">2</span><span class="s1">] + </span><span class="s2">2</span><span class="s1">*(L1[</span><span class="s2">1</span><span class="s1">]*L2[</span><span class="s2">0</span><span class="s1">] - L1[</span><span class="s2">0</span><span class="s1">]*L2[</span><span class="s2">1</span><span class="s1">])</span>
    <span class="s1">L = [a</span><span class="s0">,</span><span class="s1">b</span><span class="s0">,</span><span class="s1">c]</span>
    <span class="s0">return </span><span class="s1">L</span>

<span class="s0">def </span><span class="s1">mult(L1</span><span class="s0">, </span><span class="s1">k): </span>
    <span class="s1">a = float(k*L1[</span><span class="s2">0</span><span class="s1">])</span>
    <span class="s1">b = float(k*L1[</span><span class="s2">1</span><span class="s1">])</span>
    <span class="s1">c = float(k*k*L1[</span><span class="s2">2</span><span class="s1">])</span>
    <span class="s1">L = [a</span><span class="s0">,</span><span class="s1">b</span><span class="s0">,</span><span class="s1">c]</span>
    <span class="s0">return </span><span class="s1">L</span>

<span class="s0">def </span><span class="s1">removeDuplicates(L):</span>
    <span class="s1">T =  set(tuple(i) </span><span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">L)</span>
    <span class="s1">T2 = list(T)</span>
    <span class="s1">print(</span><span class="s4">&quot;Duplicates Removed&quot;</span><span class="s1">)</span>
    <span class="s0">return </span><span class="s1">T2</span>

<span class="s0">def </span><span class="s1">multiComb(arr</span><span class="s0">, </span><span class="s1">m): </span>
    <span class="s1">L = list(product(</span><span class="s4">'01234'</span><span class="s0">, </span><span class="s1">repeat = </span><span class="s2">7</span><span class="s1">))</span>
                    <span class="s3">#0 through m-1, m</span>
    <span class="s1">sumList = []</span>
    <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(</span><span class="s2">0</span><span class="s0">, </span><span class="s1">len(L)):</span>
        <span class="s1">sum = [</span><span class="s2">0</span><span class="s0">, </span><span class="s2">0</span><span class="s0">, </span><span class="s2">0</span><span class="s1">]</span>
        <span class="s0">for </span><span class="s1">j </span><span class="s0">in </span><span class="s1">range(</span><span class="s2">0</span><span class="s0">, </span><span class="s1">len(L[i])):</span>
            <span class="s1">sum = add(sum</span><span class="s0">, </span><span class="s1">vectors[int(L[i][j])])</span>
        <span class="s1">sumList.append(mult(sum</span><span class="s0">, </span><span class="s1">(</span><span class="s2">1</span><span class="s1">/m)))</span>
    <span class="s1">combSet = sumList</span>
    <span class="s1">print(</span><span class="s4">&quot;Combinations Done&quot;</span><span class="s1">)</span>
    <span class="s0">return </span><span class="s1">combSet</span>

<span class="s1">combSet = multiComb(vectors</span><span class="s0">, </span><span class="s1">m)</span>
<span class="s1">removeDuplicates(combSet)</span>
<span class="s1">print(</span><span class="s4">&quot;Plotting...&quot;</span><span class="s1">)</span>

<span class="s1">pg.mkQApp()</span>
<span class="s1">view = gl.GLViewWidget()</span>
<span class="s1">xgrid = gl.GLGridItem()</span>
<span class="s1">ygrid = gl.GLGridItem()</span>
<span class="s1">zgrid = gl.GLGridItem()</span>
<span class="s1">view.addItem(xgrid)</span>
<span class="s1">view.addItem(ygrid)</span>
<span class="s1">view.addItem(zgrid)</span>
<span class="s1">xgrid.rotate(</span><span class="s2">90</span><span class="s0">, </span><span class="s2">0</span><span class="s0">, </span><span class="s2">1</span><span class="s0">, </span><span class="s2">0</span><span class="s1">)</span>
<span class="s1">ygrid.rotate(</span><span class="s2">90</span><span class="s0">, </span><span class="s2">1</span><span class="s0">, </span><span class="s2">0</span><span class="s0">, </span><span class="s2">0</span><span class="s1">)</span>

<span class="s1">points = gl.GLScatterPlotItem(pos=combSet</span><span class="s0">, </span><span class="s1">color=(</span><span class="s2">1</span><span class="s0">,</span><span class="s2">1</span><span class="s0">,</span><span class="s2">1</span><span class="s0">,</span><span class="s2">1</span><span class="s1">)</span><span class="s0">, </span><span class="s1">size=</span><span class="s2">0.1</span><span class="s0">, </span><span class="s1">pxMode=</span><span class="s0">False</span><span class="s1">)</span>
<span class="s1">initials = gl.GLScatterPlotItem(pos=vectors</span><span class="s0">, </span><span class="s1">color=(</span><span class="s2">.5</span><span class="s0">,</span><span class="s2">1</span><span class="s0">,</span><span class="s2">.5</span><span class="s0">,</span><span class="s2">1</span><span class="s1">)</span><span class="s0">, </span><span class="s1">size=</span><span class="s2">1</span><span class="s0">, </span><span class="s1">pxMode=</span><span class="s0">False</span><span class="s1">)</span>
<span class="s1">view.addItem(points)</span>
<span class="s1">view.addItem(initials)</span>

<span class="s1">view.show()</span></pre>
</body>
</html>