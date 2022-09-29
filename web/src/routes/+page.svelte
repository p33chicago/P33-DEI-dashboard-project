<script>
    import {base} from '$app/paths';
    import CardText from '$lib/cards/CardText.svelte';
    import CTASection from "$lib/CTASection.svelte";
    import Takeaway from "$lib/Takeaway.svelte";
    import BodyContentContainer from "$lib/BodyContentContainer.svelte";
</script>

<svelte:head>
    <title>Home</title>
    <meta name="description" content="P33"/>
</svelte:head>

<BodyContentContainer>
    <!-- top part -->
    <h1 class="order-first col-span-1 sm:col-span-4">Our Challenge, <span class="bg-heads-up-yellow p-1">Our Opportunity</span></h1>
    <div class="col-span-1 sm:col-span-2">
        <p>
            Skilled tech jobs are fast-growing, high-paying and resilient to economic change and companies can't
            fill their roles fast enough.
            Bringing more Chicagoans into tech roles will accelerate economic growth and can address persistent
            race-based income inequality.
        </p>
        <p>
            But today, Black and Latino Chicagoans and women are dramatically underrepresented in these roles.
            If we stay on this path, tech's growth will worsen race-based inequity. But we can choose another path.
        </p>
        <p>
            This is Chicagoland's first effort to understand the full picture of what it will take to make Chicago
            the most inclusive tech city in the country.
            And to understand how we are or aren't supporting Black and Latino Chicagoans at critical moments on the
            journey from school to great jobs in the digital economy
        </p>
        <p>
            This isn't simply a "company problem" or a "pipeline problem". There is critical work to do from grammer
            school to the C-suite.
            We've gathered the data to show the way forward and offer solutions that every organization in the city
            can help move forward. Let's go make it happen!
        </p>
    </div>
    <div class="-order-1 sm:order-none col-span-1 sm:col-span-2 justify-self-center">
        <img src={`${base}/equity-diagram.png`} alt=""/>
    </div>
</BodyContentContainer>
<div class="w-full bg-brand-primary-light-green/30">
    <BodyContentContainer>
        <div>
            <CardText>
                <h2>Why it matters</h2>
                <p>
                    The future, it's where you're going? Let's get him. Go. Well, because George, nice girls get angry
                    when guys take advantage of them. Uh, you mean nobody's asked you?
                </p>
            </CardText>
        </div>
        <div>
            <CardText>
                <h2>Why it matters</h2>
                <p>
                    The future, it's where you're going? Let's get him. Go. Well, because George, nice girls get angry
                    when guys take advantage of them. Uh, you mean nobody's asked you?
                </p>
            </CardText>
        </div>
        <div>
            <CardText>
                <h2>Why it matters</h2>
                <p>
                    The future, it's where you're going? Let's get him. Go. Well, because George, nice girls get angry
                    when guys take advantage of them. Uh, you mean nobody's asked you?
                </p>
            </CardText>
        </div>
        <div>
            <CardText>
                <h2>Why it matters</h2>
                <p>
                    The future, it's where you're going? Let's get him. Go. Well, because George, nice girls get angry
                    when guys take advantage of them. Uh, you mean nobody's asked you?
                </p>
            </CardText>
        </div>
    </BodyContentContainer>
</div>
<div class="w-full bg-chicago bg-background-map bg-blend-screen bg-repeat">
    <BodyContentContainer>
        <!-- mid part -->
        <div class="py-6">
            <h1 class="text-white text-5xl col-span-1 sm:col-span-4">Scorecard</h1>
            <div class="text-white col-span-1 sm:col-span-4">pretty stuff here</div>
        </div>
    </BodyContentContainer>
</div>
<BodyContentContainer>
    <!-- bottom part -->
    <h3 class="col-span-1 sm:col-span-4">Black and Latinx Chicagoans, trans, non-binary and women remain
        underrepresented in high-paid
        technical roles</h3>

    <!-- Takeaways -->
    <div class="flex col-span-1 sm:col-span-2">
        <Takeaway heading="47% vs 14%">
            <img slot="graphic" src={`${base}/diverse-roles.svg`} class="self-start w-[64px] sm:w-[147px] aspect-square"/>
            <p>
                Nearly half the Cook County population is Black or Latino, but those groups get only 14% of the
                high-skilled tech jobs.
            </p>
        </Takeaway>
    </div>
    <div class="flex col-span-1 sm:col-span-2">
        <Takeaway heading="42% vs 22%">
            <img slot="graphic" src={`${base}/graduation-hat.svg`} class="self-start w-[64px] sm:w-[147px] aspect-square"/>
            <p>
                Illinois college graduates in computing are 22% Black or Latino despite being 42% of all Illinois high
                school graduates.
            </p>
        </Takeaway>
    </div>
    <div class="flex col-span-1 sm:col-span-2">
        <Takeaway heading="400% more">
            <img slot="graphic" src={`${base}/homogenous.svg`} class="self-start w-[64px] sm:w-[147px] aspect-square"/>
            <p>
                We’re failing kids early. Chicago needs to ensure 9,100 more Black and Latino 8th graders meet math
                proficiency standards to close gaps with other groups… And we need to get 5,500 more Black and Latino
                8th graders to advanced standards to close gaps.
            </p>
        </Takeaway>
    </div>
    <div class="flex col-span-1 sm:col-span-2">
        <Takeaway heading="5,000+">
            <img slot="graphic" src={`${base}/hands-puzzle.svg`} class="self-start w-[64px] sm:w-[147px] aspect-square"/>
            <p>
                Access to accelerated opportunities is inequitable: In order to close gaps, Chicago needs to get 5,500
                more 8th Black and Latino 8th graders to advanced standards, and enroll 5,100 more Black and Latino
                students into AP Computer Science. Right highlights: "advanced" and "AP Computer Science"
            </p>
        </Takeaway>
    </div>

    <div class="flex col-span-1 sm:col-span-4 rounded-lg bg-brand-primary-light-green/30">
        <CTASection title="What can you do to help?" href="#" link_text="see opportunities">
            <img slot="graphic" src={`${base}/chicago.svg`} class="hidden sm:block w-32 h-48 mix-blend-overlay"/>
            <p class="text-xl">Every org can play a role in building a more inclusive TechChicago</p>
        </CTASection>
    </div>
</BodyContentContainer>