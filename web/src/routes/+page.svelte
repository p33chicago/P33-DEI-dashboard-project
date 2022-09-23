<script>
    import Figure from '$lib/figure/Figure.svelte';
    import Card from '$lib/cards/Card.svelte';
	import { base } from '$app/paths';
	import CardText from '$lib/cards/CardText.svelte';
</script>

<svelte:head>
    <title>Home</title>
    <meta name="description" content="P33"/>
</svelte:head>

<!-- <div class="snap-start space-y-4 text-center h-screen">
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
</div> -->

<div class="grid grid-cols-4 gap-4 pb-64">
    <!-- top part -->
    <div class="col-span-2">
        <h1>Our Challenge, Our Opportunity</h1>
        <div>
            <p>
                I'm telling the truth, Doc, you gotta believe me. Alright, c'mon, I think we're safe. Hey George, buddy, hey, I've been looking all over for you. You remember me, the guy who saved your life the other day. Yeah but George, Lorraine wants to go with you. Give her a break. Yeah, yeah what are you wearing, Dave.
            </p>
            <p>
                Give me a hand, Lorenzo. Ow, dammit, man, I sliced my hand. What? C'mon, c'mon let's go. Um, yeah well I might have sort of ran into my parents. Oh, if Paul calls me tell him I'm working at the boutique late tonight.
            </p>
            <p>
                Hey boy, are you alright? Hey George, buddy, hey, I've been looking all over for you. You remember me, the guy who saved your life the other day. Oh. C'mon, open up, let me out of here, Yo. In that case, I'll tell you strait out.
            </p>
            <p>
                yes, Joey just loves being in his playpen. he cries whenever we take him out so we just leave him in there all the time. Well Marty, I hope you like meatloaf. What did I just say? I know, and all I could say is I'm sorry. A block passed Maple, that's John F. Kennedy Drive. Doc.
            </p>
            <p>
                Yeah but George, Lorraine wants to go with you. Give her a break. Well, you mean, it makes perfect sense. Oh yes sir. Aw yeah, everything is great. No no no this sucker's electrical, but I need a nuclear reaction to generate the one point twenty-one gigawatts of electricity that I need. 
            </p>
        </div>
    </div>
    <div class="col-span-2">
        IMAGE HERE
    </div>
    <div>
        <CardText>
            <h2>Why it matters</h2>
            <p>
                The future, it's where you're going? Let's get him. Go. Well, because George, nice girls get angry when guys take advantage of them. Uh, you mean nobody's asked you?
            </p>
        </CardText>
    </div>
    <div>
        <CardText>
            <h2>Why it matters</h2>
            <p>
                The future, it's where you're going? Let's get him. Go. Well, because George, nice girls get angry when guys take advantage of them. Uh, you mean nobody's asked you?
            </p>
        </CardText>
    </div>
    <div>
        <CardText>
            <h2>Why it matters</h2>
            <p>
                The future, it's where you're going? Let's get him. Go. Well, because George, nice girls get angry when guys take advantage of them. Uh, you mean nobody's asked you?
            </p>
        </CardText>
    </div>
    <div>
        <CardText>
            <h2>Why it matters</h2>
            <p>
                The future, it's where you're going? Let's get him. Go. Well, because George, nice girls get angry when guys take advantage of them. Uh, you mean nobody's asked you?
            </p>
        </CardText>
    </div>
    <!-- mid part -->
     <div class="col-span-4 bg-chicago bg-brand-primary-dark-green-banner-background bg-blend-screen">
       MID SECTION
     </div>
    <!-- bottom part -->
    <h3 class="col-span-4">Black and Latinx Chicagoans, trans, non-binary and women remain underrepresented in high-paid technical roles</h3>
    <div class="col-span-2">
        <div>
            <h4>47% vs 14%</h4>
            <p>Black and Latinx population...</p>
        </div>
        <div>
            <h4>47% vs 14%</h4>
            <p>Black and Latinx population...</p>
        </div>     
    </div>
    <div class="col-span-2">
        <div>
            <h4>47% vs 14%</h4>
            <p>Black and Latinx population...</p>
        </div>
        <div>
            <h4>47% vs 14%</h4>
            <p>Black and Latinx population...</p>
        </div>  
    </div>
    <div class="col-span-1">icon here</div>
    <div class="col-span-3">
        <h5>What can you do to help</h5>
        <p>Every org can play a role in building a more inclusive TechChicago</p>
        <a class="inline-block leading-8 bg-brand-primary-dark-green text-white border-2 rounded md:px-3 lg:px-4 uppercase" href="#">see opportunites</a>
    </div>
</div>
