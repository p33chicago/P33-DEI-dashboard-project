<script>
    import MathEquation from "$lib/MathEquation.svelte";
	import CardPage from "$lib/cards/CardPage.svelte";
</script>

<CardPage>
    <h1>Methodology</h1>
    <div class="col-span-1 md:col-span-4">
        <p>All data is based on a Index of Disparity constructed in a research paper (<a target="_blank"
                                                                                        href="https://open.umich.edu/sites/default/files/downloads/PublicHealthRep-Pearcy.pdf">Percy
            Keppel 2002</a>) and adopted by Policy
            Link’s <a target="_blank" href="https://nationalequityatlas.org/about-the-atlas/methodology/indexmethod">National
                Equity Index</a>.</p>
        <p>This equation is relatively simple, performs well at diagnosing inequity, and offers an unbiased approach when
            assessing different race/ethnic groups and population sizes.</p>
        <p>In short, the Index of Disparity measures the dispersion of a given subgroup (in our case race/ethnicity) around
            a
            metrics overall average. When large differences between groups are recorded, the Index will report larger
            numbers
            indicating inequity.</p>
        <p>After applying the Index of Disparity equation to each metric, we take the square root of each metric score to
            limit
            the effect of outliers on the data.</p>
        <p> We scale the numbers from 0-100 where 0 represents the largest example of disparity between race/ethnic groups
            and
            100 represents no disparity between race/ethnic groups. The 0-100 scale is used to make the data presentation
            more
            intuitive for the audience. </p>
        <p>Now that each metric score is calculated and scaled properly, we find the framework score (Proficiency,
            Excellence,
            Access) by taking the geometric mean of each metric in each framework.</p>
        <p>Lastly, we find the life stage score (K-8, HS, College, Career) by taking the geometric mean of each framework
            score
            in each life stage.</p>
        <p class="text-xl py-4"> <MathEquation math={`Index~of~disparity = \\frac{\\sum{[|r_i - R|]}}{R * N}`} /> </p>
        <p class="text-xl py-4"> <MathEquation math={`Geometric Mean = \\sqrt[N]{x_1 * x_2 * ... * x_N}`} /> </p>
        <p class="text-xl py-4"> <MathEquation math={`Scaling Equation = 100 - \\frac{Index~of~Disparity_i - Min(Index~of~Disparity)}{Max(Index~of~Disparity)}`} /> </p>
    </div>
</CardPage>