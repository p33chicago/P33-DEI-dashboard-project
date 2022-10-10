<script type="ts">
	import Card from '../../lib/cards/Card.svelte';
	import MathEquation from '../../lib/MathEquation.svelte';
</script>

<Card>
	<div class="block p-4 lg:p-10 bg-white">
		<h1 class="pb-2">Methodology</h1>
		<hr class="border-1 border-light-gray" />
		<div class="col-span-1 md:col-span-4">
			<p class="bg-really-light-gray my-8 pl-6 pr-2 py-4 font-mono">
				The Equity Index scores are based on more than 20 individual metrics secured primarily from
				government and other official sources, using the latest available data for each metric. We
				intend to add additional metrics, comparisons with individual cities, and data to show
				progress over time.
			</p>
			<p>
				All data is based on a Index of Disparity constructed in a research paper (<a
					target="_blank"
					href="https://open.umich.edu/sites/default/files/downloads/PublicHealthRep-Pearcy.pdf"
					class="text-brand-primary-green">Percy Keppel 2002</a
				>) and adopted by Policy Link’s
				<a
					target="_blank"
					href="https://nationalequityatlas.org/about-the-atlas/methodology/indexmethod"
					class="text-brand-primary-green">National Equity Index</a
				>.
			</p>
			<p>
				This equation is relatively simple, performs well at diagnosing inequity, and offers an
				unbiased approach when assessing different race/ethnic groups and population sizes.
			</p>
			<p>
				In short, the Index of Disparity measures the dispersion of a given subgroup (in our case
				race/ethnicity) around a metrics overall average. When large differences between groups are
				recorded, the Index will report larger numbers indicating inequity.
			</p>
			<p>
				After applying the Index of Disparity equation to each metric, we take the square root of
				each metric score to limit the effect of outliers on the data.
			</p>
			<p>
				We scale the numbers from 0-100 where 0 represents the largest example of disparity between
				race/ethnic groups and 100 represents no disparity between race/ethnic groups. The 0-100
				scale is used to make the data presentation more intuitive for the audience.
			</p>
			<p>
				Now that each metric score is calculated and scaled properly, we find the framework score
				(Proficiency, Excellence, Access) by taking the geometric mean of each metric in each
				framework.
			</p>
			<p>
				Lastly, we find the life stage score (K-8, HS, College, Career) by taking the geometric mean
				of each framework score in each life stage.
			</p>
			<div class="bg-really-light-gray mt-10">
				<h2 class="uppercase p-4 text-center font-sans-alternate">index calculation</h2>
				<p class="py-2 text-center font-sans-alternate">
					<MathEquation math={`Index~of~disparity = \\frac{\\sum{[|r_i - R|]}}{R * N}`} />
				</p>
				<p class="py-2 text-center font-sans-alternate">
					<MathEquation math={`Geometric Mean = \\sqrt[N]{x_1 * x_2 * ... * x_N}`} />
				</p>
				<p class="py-6 text-center font-sans-alternate">
					<MathEquation
						math={`Scaling Equation = 100 - \\frac{Index~of~Disparity_i - Min(Index~of~Disparity)}{Max(Index~of~Disparity)}`}
					/>
				</p>
				<hr class="border-1 border-light-gray mx-4" />
				<div class="p-6">
					<p>
						<span class="text-brand-primary-green">Proficiency:</span> How well are we preparing Black
						and Latino students to pursue and succeed on Computer Science pathways?
					</p>
					<p>
						<span class="text-brand-primary-green">Access:</span> How much access do Black and Latino
						communities have to the resources and opportunities necessary to succeed on Computer Science
						pathways?
					</p>
					<p>
						<span class="text-brand-primary-green">Excellence:</span> How well are we preparing Black
						and Latino students to succeed at elite levels on Computer Science pathways?
					</p>
				</div>
			</div>
		</div>
	</div>
</Card>
