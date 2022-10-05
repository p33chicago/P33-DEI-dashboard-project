<script type="ts">
    import DataSidebar from "$lib/DataSidebar.svelte";
    import IndicatorNav from '$lib/IndicatorNav.svelte';
    import IndicatorContent from "$lib/indicators/IndicatorContent.svelte";
    import BodyContentContainer from "$lib/BodyContentContainer.svelte";
    import BannerTitle from "$lib/BannerTitle.svelte";

    export let data;

    $: lifestage = data.lifestage;
    $: indicator = data.indicator
</script>

<svelte:head>
    <title>{lifestage.name}: {indicator.name}</title>
</svelte:head>

<BannerTitle
        title={lifestage.name}
        subtitle="Equity index scorecard"
/>

<BodyContentContainer>
    <DataSidebar {lifestage}/>

    <IndicatorNav {lifestage} {indicator}/>

    <div class="grid auto-rows-min row-span-2 col-span-4 md:col-span-3 gap-y-4">
        <IndicatorContent active_indicator={indicator}>
            <slot/>
        </IndicatorContent>
    </div>
</BodyContentContainer>
