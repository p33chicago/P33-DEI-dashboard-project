<script type="ts">
    import type {Scorecard} from "$lib/domain/Scorecard";

    export let indicators: Scorecard[number]['indicators'];
</script>

{#each indicators as indicator}
    <div>
        {indicator.name}
    </div>
{/each}