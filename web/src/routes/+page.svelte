<script>
    import Figure from '$lib/figure/Figure.svelte';
    import Card from '$lib/cards/Card.svelte';
	import { base } from '$app/paths';
</script>

<svelte:head>
    <title>Home</title>
    <meta name="description" content="P33"/>
</svelte:head>

<div class="snap-start space-y-4 text-center h-screen">
    <Card>
		<h1 class="capitalize"><a href={`${base}/k8/access`}>K-8</a></h1>
        <p>City of Chicago</p>
    </Card>
    <Card>
        <Figure id="figure"/>
    </Card>
</div>
<div class="snap-start space-y-4 text-center h-screen">
    <Card>
		<h1 class="capitalize"><a href={`${base}/hs/access`}>High school</a></h1>
        <p>City of Chicago</p>
    </Card>
    <Card>
        <Figure id="figure"/>
    </Card>
</div>
<div class="snap-start space-y-4 text-center h-screen">
    <Card>
		<h1 class="capitalize"><a href={`${base}/college/access`}>College</a></h1>
        <p>City of Chicago</p>
    </Card>
    <Card>
        <Figure id="figure"/>
    </Card>
</div>
<div class="snap-start space-y-4 text-center h-screen">
    <Card>
		<h1 class="capitalize"><a href={`${base}/career/access`}>Career</a></h1>
        <p>City of Chicago</p>
    </Card>
    <Card>
        <Figure id="figure"/>
    </Card>
</div>
