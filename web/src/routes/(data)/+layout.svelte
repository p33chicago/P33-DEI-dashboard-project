<script type="ts">
    import {indicators} from '$lib/domain/Indicator.ts';
    import DataSidebar from "$lib/DataSidebar.svelte";
    import IndicatorContent from "$lib/indicators/IndicatorContent.svelte";
    import {base} from '$app/paths';
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

<div class="font-sans-alternate bg-chicago bg-brand-primary-dark-green-banner-background bg-blend-screen bg-repeat">
    <BodyContentContainer>
        <div class="col-span-4">
            <h1 class="text-white">Kindergarten-8th, High School, College, Career</h1>
            <h2 class="text-heads-up-yellow">Equity index scorecard</h2>
        </div>
    </BodyContentContainer>
</div>

<BodyContentContainer>
    <DataSidebar {lifestage}/>

    {#if lifestage}
        <div class="hidden md:block col-start-2 col-span-3 2xl:w-screen">
            {#each indicators as _indicator}
                <a
                        class="inline-block leading-8 bg-white border-2 rounded-full md:px-3 lg:px-6 uppercase"
                        class:border-brand-primary-dark-green={_indicator.route === indicator.route}
                        class:bg-brand-primary-dark-green={_indicator.route === indicator.route}
                        class:text-white={_indicator.route === indicator.route}
                        href={`${base}/${lifestage.route}/${_indicator.route}`}
                >{_indicator.name}</a>
            {/each}
        </div>
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
