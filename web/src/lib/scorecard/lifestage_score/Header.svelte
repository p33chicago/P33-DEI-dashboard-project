<script type="ts">
    import type {Lifestage} from "$lib/domain/Lifestage";

    export let lifestage: Lifestage;
    export let area: string;
    export let score: number;
</script>
<div class="flex">
    <div>img</div>
    <div class="grow">
        <h1 class="text-2xl text-black">{lifestage.name}</h1>
        <h2 class="text-sm uppercase font-sans-alternate text-dark-gray">{area}</h2>
    </div>
    <div class="text-right relative">
        <span class="block text-5xl text-brand-primary-dark-green">{score}</span>
        <span class="block absolute right-0 overflow-hidden bg-medium-gray h-[1px] w-10">/</span>
        <span class="block text-dark-gray">100</span>
        <span class="block text-dark-gray text-xs">Equity Index</span>
    </div>
</div>