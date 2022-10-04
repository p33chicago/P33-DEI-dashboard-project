<script type="ts">
    import type {Scorecard} from "$lib/domain/Scorecard";

    export let indicators: Scorecard[number]['indicators'];
</script>

{#each indicators as indicator}
    <div class="flex">
        <div class="text-sm grow">
            {indicator.name}
        </div>
        <div class="text-sm">
            {indicator.score}
        </div>
    </div>
    <div class="h-[4px] bg-light-gray">
        {#if indicator.name === 'Access'}
            <div class="bg-blue h-full" style={`width: ${indicator.score}%`}></div>
        {:else if indicator.name === 'Proficiency' }
            <div class="bg-brand-primary-dark-green h-full" style={`width: ${indicator.score}%`}></div>
        {:else}
            <div class="bg-warn-orange h-full" style={`width: ${indicator.score}%`}></div>
        {/if}
    </div>
{/each}