<div class="container">
    <!-- ie: methodology -->
    <slot name="title" />
    <!-- ie: 2 cols; metrics and Qs -->
    <div>
        <div>
            <slot name="metrics" />
        </div>
        <div>
            <slot name="info" />
        </div>
    </div>
    <!-- ie: summary/ answers to those intro Qs? -->
    <div>
        <slot name="summary" />
    </div>
</div>