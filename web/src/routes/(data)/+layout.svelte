<script type="ts">
    import DataSidebar from "$lib/DataSidebar.svelte";
    import IndicatorNav from '$lib/IndicatorNav.svelte';
    import IndicatorContent from "$lib/indicators/IndicatorContent.svelte";
    import BodyContentContainer from "$lib/BodyContentContainer.svelte";

    export let data;

    let lifestage, indicator, title;
    $: {
        lifestage = data.lifestage;
        indicator = data.indicator;
        title = lifestage ? lifestage.name : 'Scorecard';
        if (indicator) {
            title += `: ${indicator.name}`;
        }
    }
</script>

<svelte:head>
    <title>{title}</title>
</svelte:head>

<div class="font-sans-alternate bg-chicago bg-background-map bg-blend-screen bg-repeat">
    <BodyContentContainer>
        <div class="col-span-4">
            <h1 class="text-white">Kindergarten-8th, High School, College, Career</h1>
            <h2 class="text-heads-up-yellow">Equity index scorecard</h2>
        </div>
    </BodyContentContainer>
</div>

<BodyContentContainer>
    <DataSidebar {lifestage}/>

    {#if lifestage }
        <IndicatorNav {lifestage} {indicator} />
    {/if}

    <div class="grid auto-rows-min row-span-2 col-span-4 md:col-span-3 gap-y-4">
        {#if indicator}
            <IndicatorContent active_indicator={indicator}>
                <slot/>
            </IndicatorContent>
        {:else}
            <slot/>
        {/if}
    </div>
</BodyContentContainer>
