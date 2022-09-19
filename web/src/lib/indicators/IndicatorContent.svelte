<script type="ts">
    import type {Indicator} from "$lib/domain/Indicator.ts";
    import IndicatorCard from "$lib/cards/IndicatorCard.svelte";
    import AccessSnippet from "$lib/indicators/snippets/AccessSnippet.svelte";
    import ProficiencySnippet from "$lib/indicators/snippets/ProficiencySnippet.svelte";
    import ExcellenceSnippet from "$lib/indicators/snippets/ExcellenceSnippet.svelte";
    import {indicators, access, excellence, proficiency} from "$lib/domain/Indicator.ts";

    export let active_indicator: Indicator;
</script>

{#each indicators as indicator}
    {#if active_indicator.name === indicator.name}
        <IndicatorCard>
            {#if indicator === access}
                <AccessSnippet score="20.1"/>
            {:else if indicator === proficiency}
                <ProficiencySnippet score="20.1"/>
            {:else}
                <ExcellenceSnippet score="20.1"/>
            {/if}

            <slot/>
        </IndicatorCard>
    {:else}
        <a href={indicator.route} class="md:hidden">
            <IndicatorCard>
                {#if indicator === access}
                    <AccessSnippet score="20.1"/>
                {:else if indicator === proficiency}
                    <ProficiencySnippet score="20.1"/>
                {:else}
                    <ExcellenceSnippet score="20.1"/>
                {/if}
            </IndicatorCard>
        </a>
    {/if}
{/each}
