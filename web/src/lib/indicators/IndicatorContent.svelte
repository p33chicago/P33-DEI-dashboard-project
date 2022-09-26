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
                <AccessSnippet/>
            {:else if indicator === proficiency}
                <ProficiencySnippet/>
            {:else}
                <ExcellenceSnippet/>
            {/if}

            <slot/>
        </IndicatorCard>
    {:else}
        <a href={indicator.route} class="md:hidden">
            <IndicatorCard>
                {#if indicator === access}
                    <AccessSnippet/>
                {:else if indicator === proficiency}
                    <ProficiencySnippet/>
                {:else}
                    <ExcellenceSnippet/>
                {/if}
            </IndicatorCard>
        </a>
    {/if}
{/each}
