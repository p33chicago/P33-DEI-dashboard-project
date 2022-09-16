<!--<script type="ts">-->
<!--    import Card from "$lib/cards/Card.svelte";-->

<!--    export let title: string;-->
<!--    export let route: string;-->
<!--    export let current_indicator: string;-->
<!--    export let base: string;-->
<!--    $: active = current_indicator.includes(route);-->
<!--    const link_target = active ? base : `${base}/${route}`-->
<!--    $: console.log(title, route, current_indicator, active)-->
<!--</script>-->

<!--<Card>-->
<!--    <a href={link_target} class="text-dark-gray">-->
<!--        <h1>{title}</h1>-->
<!--        <slot/>-->
<!--        {#if active }-->
<!--            <slot name="more"/>-->
<!--        {/if}-->
<!--    </a>-->
<!--</Card>-->
High School: Access