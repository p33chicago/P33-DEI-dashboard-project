<script type="ts">
    import Card from "./Card.svelte";

    export let title: string;
</script>

<Card>
    <slot/>
    {#if $$slots.more }
        <slot name="more"/>
    {/if}
</Card>
