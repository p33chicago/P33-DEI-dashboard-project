<script>
    import Card from './cards/Card.svelte'
    import { base } from '$app/paths'
</script>

<div class="hidden md:grid col-span-1 row-span-2 text-xl auto-rows-min gap-4">
    <Card>
        <ul>
            <li class="uppercase py-1"><a href={`${base}/k8/access`}>k-8</a></li>
            <li class="uppercase py-1"><a href={`${base}/hs/access`}>highschool</a></li>
            <li class="uppercase py-1"><a href={`${base}/college/access`}>college</a></li>
            <li class="uppercase py-1"><a href={`${base}/career/access`}>career</a></li>
            <li class="uppercase py-1"><a href={base}>scorecard</a></li>
        </ul>
    </Card>
    <div class="bg-brand-primary-dark-green-banner-background text-white px-6 py-6">
        <h1>Life Stages</h1>
        <div class="py-4 text-base text-light-gray">
            <p>Magnet school enrollment rate relative to population size in...</p>
        </div>
        <div class="text-base text-light-gray">
            <p>Learn more about equity index</p>
        </div>
    </div>
</div>