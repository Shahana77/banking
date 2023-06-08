<script type="text/javascript">
    //<![CDATA[
    $(function () {
        var $cat = $("#country"),
            $state = $(".state");
        var optgroups = {};
        $state.each(function (i, v) {
            var $e = $(v);
            var _id = $e.attr("id");
            optgroups[_id] = {};
            $e.find("optgroup").each(function () {
                var _r = $(this).data("rel");
                $(this).find("option").addClass("is-dyn");
                optgroups[_id][_r] = $(this).html();
            });
        });
        $state.find("optgroup").remove();

        var _lastRel;
        $cat.on("change", function () {
            var _rel = $(this).val();
            if (_lastRel === _rel) return true;
            _lastRel = _rel;
            $state.find("option").attr("style", "");
            $state.val("");
            $state.find(".is-dyn").remove();
            if (!_rel) return $state.prop("disabled", true);
            $state.each(function () {
                var $el = $(this);
                var _id = $el.attr("id");
                $el.append(optgroups[_id][_rel]);
            });
            $state.prop("disabled", false);
        });
    });
    //]]>
</script>
