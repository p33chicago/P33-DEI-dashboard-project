<script lang="ts">
    import Card from './cards/Card.svelte'
    export let access: string;
    export let proficiency: string;
    export let excellence: string;
</script>

<Card>
    <p>access: {access}</p>
    <p>proficiency: {proficiency}</p>
    <p>excellence: {excellence}</p>
</Card>
			
