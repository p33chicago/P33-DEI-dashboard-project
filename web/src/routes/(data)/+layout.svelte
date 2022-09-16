<script type="ts">
    import type {Indicator} from '$lib/domain/Indicator.ts';
    import {indicators} from '$lib/domain/Indicator.ts';
    import DataSidebar from "$lib/DataSidebar.svelte";
    import LifestageTitleCard from "$lib/LifestageTitleCard.svelte";
    import LifestageIndexCard from "$lib/LifestageIndexCard.svelte";
    import LifestageIndicatorsCard from "$lib/LifestageIndicatorsCard.svelte";
    import {base} from '$app/paths';

    export let data;

    const {lifestage, indicator} = data;
    let title = lifestage.name;
    if (indicator) {
        title += `: ${indicator.name}`;
    }

    const is_active = (candidate_indicator: Indicator) => candidate_indicator.route === indicator.route;
</script>

<svelte:head>
    <title>{title}</title>
</svelte:head>

<a href={`${base}/`} class="leading-8 hidden md:grid col-span-1">&larr; Back</a>
<div class="hidden md:block col-span-3 2xl:w-screen">
    {#each indicators as indicator}
        <a
                class="inline-block leading-8 bg-white border-2 rounded-full md:px-3 lg:px-6 uppercase"
                class:bg-brand-primary-dark-green={is_active(indicator)}
                class:text-white={is_active(indicator)}
                href={`${base}/${lifestage.route}/${indicator.route}`}
        >{indicator.name}</a>
    {/each}
</div>

<DataSidebar>
    <LifestageTitleCard slot="title" title={lifestage.name}/>
    <LifestageIndexCard slot="index" chicago="40" us="70"/>
    <LifestageIndicatorsCard slot="indicators" access="10" excellence="1" proficiency="2"/>
</DataSidebar>
<div class="col-span-4 md:col-span-3 space-y-6">
    <slot/>
</div>
