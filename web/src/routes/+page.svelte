<script>
    import {base} from '$app/paths';
    import CardText from '$lib/cards/CardText.svelte';
    import CTASection from "$lib/CTASection.svelte";
</script>

<svelte:head>
    <title>Home</title>
    <meta name="description" content="P33"/>
</svelte:head>

<div class="grid grid-cols-4 gap-4 pb-64 px-24 pt-8">
    <!-- top part -->
    <div class="col-span-2">
        <h1>Our Challenge, <span class="bg-heads-up-yellow p-1">Our Opportunity</span></h1>
        <div>
            <p>
                Skilled tech jobs are fast-growing, high-paying and resilient to economic change and companies can't fill their roles fast enough.
                Bringing more Chicagoans into tech roles will accelerate economic growth and can address persistent race-based income inequality.
            </p>
            <p>
                But today, Black and Latino Chicagoans and women are dramatically underrepresented in these roles.
                If we stay on this path, tech's growth will worsen race-based inequity. But we can choose another path.
            </p>
            <p>
                This is Chicagoland's first effort to understand the full picture of what it will take to make Chicago the most inclusive tech city in the country.
                And to understand how we are or aren't supporting Black and Latino Chicagoans at critical moments on the journey from school to great jobs in the digital economy
            </p>
            <p>
                This isn't simply a "company problem" or a "pipeline problem". There is critical work to do from grammer school to the C-suite.
                We've gathered the data to show the way forward and offer solutions that every organization in the city can help move forward. Let's go make it happen!
            </p>
        </div>
    </div>
    <div class="col-span-2 justify-self-center">
        <img src={`${base}/equity-diagram.png`} alt="" />
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
    <CTASection title="What can you do to help?" href="#" link_text="see opportunities">
        <img slot="graphic" src="/chicago.svg" class="w-32 h-48 mix-blend-overlay" />
        <p>Every org can play a role in building a more inclusive TechChicago</p>
    </CTASection>
</div>
