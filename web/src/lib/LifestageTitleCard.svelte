<script lang="ts">
    import Card from './cards/Card.svelte'
    export let title: string;
    let subtitle: string = "Chicago Public Schools";
</script>

<Card>
    <h1 class="capitalize">{title}</h1>
    <p>{subtitle}</p>
</Card>
			
