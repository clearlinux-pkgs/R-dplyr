#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dplyr
Version  : 0.8.0.1
Release  : 29
URL      : https://cran.r-project.org/src/contrib/dplyr_0.8.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dplyr_0.8.0.1.tar.gz
Summary  : A fast, consistent tool for working with data frame like objects.
Group    : Development/Tools
License  : MIT
Requires: R-dplyr-lib = %{version}-%{release}
Requires: R-pillar
Requires: R-purrr
BuildRequires : R-BH
BuildRequires : R-bindrcpp
BuildRequires : R-glue
BuildRequires : R-pillar
BuildRequires : R-pkgconfig
BuildRequires : R-plogr
BuildRequires : R-purrr
BuildRequires : R-tibble
BuildRequires : R-tidyselect
BuildRequires : buildreq-R

%description
# dplyr <a href='https:/dplyr.tidyverse.org'><img src='man/figures/logo.png' align="right" height="139" /></a>

%package lib
Summary: lib components for the R-dplyr package.
Group: Libraries

%description lib
lib components for the R-dplyr package.


%prep
%setup -q -c -n dplyr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556472791

%install
export SOURCE_DATE_EPOCH=1556472791
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dplyr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dplyr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dplyr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dplyr/DESCRIPTION
/usr/lib64/R/library/dplyr/INDEX
/usr/lib64/R/library/dplyr/LICENSE
/usr/lib64/R/library/dplyr/Meta/Rd.rds
/usr/lib64/R/library/dplyr/Meta/data.rds
/usr/lib64/R/library/dplyr/Meta/features.rds
/usr/lib64/R/library/dplyr/Meta/hsearch.rds
/usr/lib64/R/library/dplyr/Meta/links.rds
/usr/lib64/R/library/dplyr/Meta/nsInfo.rds
/usr/lib64/R/library/dplyr/Meta/package.rds
/usr/lib64/R/library/dplyr/Meta/vignette.rds
/usr/lib64/R/library/dplyr/NAMESPACE
/usr/lib64/R/library/dplyr/NEWS.md
/usr/lib64/R/library/dplyr/R/dplyr
/usr/lib64/R/library/dplyr/R/dplyr.rdb
/usr/lib64/R/library/dplyr/R/dplyr.rdx
/usr/lib64/R/library/dplyr/data/Rdata.rdb
/usr/lib64/R/library/dplyr/data/Rdata.rds
/usr/lib64/R/library/dplyr/data/Rdata.rdx
/usr/lib64/R/library/dplyr/doc/compatibility.R
/usr/lib64/R/library/dplyr/doc/compatibility.Rmd
/usr/lib64/R/library/dplyr/doc/compatibility.html
/usr/lib64/R/library/dplyr/doc/dplyr.R
/usr/lib64/R/library/dplyr/doc/dplyr.Rmd
/usr/lib64/R/library/dplyr/doc/dplyr.html
/usr/lib64/R/library/dplyr/doc/index.html
/usr/lib64/R/library/dplyr/doc/programming.R
/usr/lib64/R/library/dplyr/doc/programming.Rmd
/usr/lib64/R/library/dplyr/doc/programming.html
/usr/lib64/R/library/dplyr/doc/two-table.R
/usr/lib64/R/library/dplyr/doc/two-table.Rmd
/usr/lib64/R/library/dplyr/doc/two-table.html
/usr/lib64/R/library/dplyr/doc/window-functions.R
/usr/lib64/R/library/dplyr/doc/window-functions.Rmd
/usr/lib64/R/library/dplyr/doc/window-functions.html
/usr/lib64/R/library/dplyr/help/AnIndex
/usr/lib64/R/library/dplyr/help/aliases.rds
/usr/lib64/R/library/dplyr/help/dplyr.rdb
/usr/lib64/R/library/dplyr/help/dplyr.rdx
/usr/lib64/R/library/dplyr/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/dplyr/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/dplyr/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/dplyr/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/dplyr/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/dplyr/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/dplyr/help/figures/lifecycle-retired.svg
/usr/lib64/R/library/dplyr/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/dplyr/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/dplyr/help/figures/logo.png
/usr/lib64/R/library/dplyr/help/paths.rds
/usr/lib64/R/library/dplyr/html/00Index.html
/usr/lib64/R/library/dplyr/html/R.css
/usr/lib64/R/library/dplyr/include/dplyr.h
/usr/lib64/R/library/dplyr/include/dplyr/Collecter.h
/usr/lib64/R/library/dplyr/include/dplyr/Groups.h
/usr/lib64/R/library/dplyr/include/dplyr/NamedListAccumulator.h
/usr/lib64/R/library/dplyr/include/dplyr/allow_list.h
/usr/lib64/R/library/dplyr/include/dplyr/checks.h
/usr/lib64/R/library/dplyr/include/dplyr/config.h
/usr/lib64/R/library/dplyr/include/dplyr/data/DataMask.h
/usr/lib64/R/library/dplyr/include/dplyr/data/GroupedDataFrame.h
/usr/lib64/R/library/dplyr/include/dplyr/data/NaturalDataFrame.h
/usr/lib64/R/library/dplyr/include/dplyr/data/RowwiseDataFrame.h
/usr/lib64/R/library/dplyr/include/dplyr/dplyr.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/Column.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/Dispatch.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/Expression.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/HybridVectorScalarResult.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/HybridVectorSummaryRecycleResult.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/HybridVectorVectorResult.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/hybrid.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/scalar_result/first_last.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/scalar_result/group_indices.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/scalar_result/mean_sd_var.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/scalar_result/min_max.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/scalar_result/n.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/scalar_result/n_distinct.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/scalar_result/sum.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/vector_result/echo.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/vector_result/in.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/vector_result/lead_lag.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/vector_result/ntile.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/vector_result/rank.h
/usr/lib64/R/library/dplyr/include/dplyr/hybrid/vector_result/row_number.h
/usr/lib64/R/library/dplyr/include/dplyr/lifecycle.h
/usr/lib64/R/library/dplyr/include/dplyr/main.h
/usr/lib64/R/library/dplyr/include/dplyr/registration.h
/usr/lib64/R/library/dplyr/include/dplyr/standard/GroupedCallReducer.h
/usr/lib64/R/library/dplyr/include/dplyr/symbols.h
/usr/lib64/R/library/dplyr/include/dplyr/visitor_set/VisitorEqualPredicate.h
/usr/lib64/R/library/dplyr/include/dplyr/visitor_set/VisitorHash.h
/usr/lib64/R/library/dplyr/include/dplyr/visitor_set/VisitorSetEqual.h
/usr/lib64/R/library/dplyr/include/dplyr/visitor_set/VisitorSetEqualPredicate.h
/usr/lib64/R/library/dplyr/include/dplyr/visitor_set/VisitorSetGreater.h
/usr/lib64/R/library/dplyr/include/dplyr/visitor_set/VisitorSetHash.h
/usr/lib64/R/library/dplyr/include/dplyr/visitor_set/VisitorSetHasher.h
/usr/lib64/R/library/dplyr/include/dplyr/visitor_set/VisitorSetIndexMap.h
/usr/lib64/R/library/dplyr/include/dplyr/visitor_set/VisitorSetIndexSet.h
/usr/lib64/R/library/dplyr/include/dplyr/visitor_set/VisitorSetLess.h
/usr/lib64/R/library/dplyr/include/dplyr/visitor_set/visitor_set.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/CharacterVectorOrderer.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/Comparer.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/SliceVisitor.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/join/Column.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/join/DataFrameJoinVisitors.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/join/JoinVisitor.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/join/JoinVisitorImpl.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/join/join_match.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/order/Order.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/order/OrderVisitor.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/order/OrderVisitorImpl.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/subset/DataFrameSelect.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/subset/DataFrameSubsetVisitors.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/subset/column_subset.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/vector/DataFrameColumnVisitor.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/vector/DataFrameVisitors.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/vector/MatrixColumnVisitor.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/vector/MultipleVectorVisitors.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/vector/VectorVisitor.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/vector/VectorVisitorImpl.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/vector/visitor.h
/usr/lib64/R/library/dplyr/include/dplyr/visitors/vector/visitor_impl.h
/usr/lib64/R/library/dplyr/include/dplyr/workarounds/installChar.h
/usr/lib64/R/library/dplyr/include/dplyr/workarounds/static_assert.h
/usr/lib64/R/library/dplyr/include/dplyr/workarounds/xlen.h
/usr/lib64/R/library/dplyr/include/dplyr_RcppExports.h
/usr/lib64/R/library/dplyr/include/dplyr_types.h
/usr/lib64/R/library/dplyr/include/solaris/solaris.h
/usr/lib64/R/library/dplyr/include/tools/BoolResult.h
/usr/lib64/R/library/dplyr/include/tools/Quosure.h
/usr/lib64/R/library/dplyr/include/tools/SlicingIndex.h
/usr/lib64/R/library/dplyr/include/tools/SymbolMap.h
/usr/lib64/R/library/dplyr/include/tools/SymbolString.h
/usr/lib64/R/library/dplyr/include/tools/SymbolVector.h
/usr/lib64/R/library/dplyr/include/tools/VectorView.h
/usr/lib64/R/library/dplyr/include/tools/all_na.h
/usr/lib64/R/library/dplyr/include/tools/bad.h
/usr/lib64/R/library/dplyr/include/tools/collapse.h
/usr/lib64/R/library/dplyr/include/tools/comparisons.h
/usr/lib64/R/library/dplyr/include/tools/debug.h
/usr/lib64/R/library/dplyr/include/tools/default_value.h
/usr/lib64/R/library/dplyr/include/tools/encoding.h
/usr/lib64/R/library/dplyr/include/tools/hash.h
/usr/lib64/R/library/dplyr/include/tools/match.h
/usr/lib64/R/library/dplyr/include/tools/pointer_vector.h
/usr/lib64/R/library/dplyr/include/tools/rlang-export.h
/usr/lib64/R/library/dplyr/include/tools/scalar_type.h
/usr/lib64/R/library/dplyr/include/tools/set_rownames.h
/usr/lib64/R/library/dplyr/include/tools/tools.h
/usr/lib64/R/library/dplyr/include/tools/train.h
/usr/lib64/R/library/dplyr/include/tools/utils.h
/usr/lib64/R/library/dplyr/include/tools/vector_class.h
/usr/lib64/R/library/dplyr/tests/testthat.R
/usr/lib64/R/library/dplyr/tests/testthat/helper-astyle.R
/usr/lib64/R/library/dplyr/tests/testthat/helper-combine.R
/usr/lib64/R/library/dplyr/tests/testthat/helper-dplyr.R
/usr/lib64/R/library/dplyr/tests/testthat/helper-encoding.R
/usr/lib64/R/library/dplyr/tests/testthat/helper-groups.R
/usr/lib64/R/library/dplyr/tests/testthat/helper-hybrid.R
/usr/lib64/R/library/dplyr/tests/testthat/helper-torture.R
/usr/lib64/R/library/dplyr/tests/testthat/test-DBI.R
/usr/lib64/R/library/dplyr/tests/testthat/test-active-bindings.R
/usr/lib64/R/library/dplyr/tests/testthat/test-arrange.r
/usr/lib64/R/library/dplyr/tests/testthat/test-astyle.R
/usr/lib64/R/library/dplyr/tests/testthat/test-between.R
/usr/lib64/R/library/dplyr/tests/testthat/test-binds.R
/usr/lib64/R/library/dplyr/tests/testthat/test-case-when.R
/usr/lib64/R/library/dplyr/tests/testthat/test-coalesce.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-arrange.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-distinct.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-filter.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-group-by.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-mutate.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-select.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise.R
/usr/lib64/R/library/dplyr/tests/testthat/test-combine.R
/usr/lib64/R/library/dplyr/tests/testthat/test-copy_to.R
/usr/lib64/R/library/dplyr/tests/testthat/test-copying.R
/usr/lib64/R/library/dplyr/tests/testthat/test-count-tally.r
/usr/lib64/R/library/dplyr/tests/testthat/test-data_frame.R
/usr/lib64/R/library/dplyr/tests/testthat/test-distinct.R
/usr/lib64/R/library/dplyr/tests/testthat/test-do.R
/usr/lib64/R/library/dplyr/tests/testthat/test-empty-groups.R
/usr/lib64/R/library/dplyr/tests/testthat/test-equality.r
/usr/lib64/R/library/dplyr/tests/testthat/test-filter.r
/usr/lib64/R/library/dplyr/tests/testthat/test-funs-predicates.R
/usr/lib64/R/library/dplyr/tests/testthat/test-funs.R
/usr/lib64/R/library/dplyr/tests/testthat/test-group-by.r
/usr/lib64/R/library/dplyr/tests/testthat/test-group-indices.R
/usr/lib64/R/library/dplyr/tests/testthat/test-group-size.R
/usr/lib64/R/library/dplyr/tests/testthat/test-group_data.R
/usr/lib64/R/library/dplyr/tests/testthat/test-group_keys.R
/usr/lib64/R/library/dplyr/tests/testthat/test-group_map.R
/usr/lib64/R/library/dplyr/tests/testthat/test-group_nest.R
/usr/lib64/R/library/dplyr/tests/testthat/test-group_split.R
/usr/lib64/R/library/dplyr/tests/testthat/test-group_trim.R
/usr/lib64/R/library/dplyr/tests/testthat/test-hybrid-traverse.R
/usr/lib64/R/library/dplyr/tests/testthat/test-hybrid.R
/usr/lib64/R/library/dplyr/tests/testthat/test-if-else.R
/usr/lib64/R/library/dplyr/tests/testthat/test-internals.r
/usr/lib64/R/library/dplyr/tests/testthat/test-joins.r
/usr/lib64/R/library/dplyr/tests/testthat/test-lazyeval-compat.R
/usr/lib64/R/library/dplyr/tests/testthat/test-lead-lag.R
/usr/lib64/R/library/dplyr/tests/testthat/test-mutate-windowed.R
/usr/lib64/R/library/dplyr/tests/testthat/test-mutate.r
/usr/lib64/R/library/dplyr/tests/testthat/test-n_distinct.R
/usr/lib64/R/library/dplyr/tests/testthat/test-na-if.R
/usr/lib64/R/library/dplyr/tests/testthat/test-near.R
/usr/lib64/R/library/dplyr/tests/testthat/test-new_grouped_df.R
/usr/lib64/R/library/dplyr/tests/testthat/test-nth-value.R
/usr/lib64/R/library/dplyr/tests/testthat/test-overscope.R
/usr/lib64/R/library/dplyr/tests/testthat/test-pull.R
/usr/lib64/R/library/dplyr/tests/testthat/test-rank.R
/usr/lib64/R/library/dplyr/tests/testthat/test-rbind.R
/usr/lib64/R/library/dplyr/tests/testthat/test-recode.R
/usr/lib64/R/library/dplyr/tests/testthat/test-sample.R
/usr/lib64/R/library/dplyr/tests/testthat/test-select.r
/usr/lib64/R/library/dplyr/tests/testthat/test-sets.R
/usr/lib64/R/library/dplyr/tests/testthat/test-slice.r
/usr/lib64/R/library/dplyr/tests/testthat/test-summarise.r
/usr/lib64/R/library/dplyr/tests/testthat/test-tbl-cube.R
/usr/lib64/R/library/dplyr/tests/testthat/test-tbl.R
/usr/lib64/R/library/dplyr/tests/testthat/test-top-n.R
/usr/lib64/R/library/dplyr/tests/testthat/test-transmute.R
/usr/lib64/R/library/dplyr/tests/testthat/test-ts.R
/usr/lib64/R/library/dplyr/tests/testthat/test-underscore.R
/usr/lib64/R/library/dplyr/tests/testthat/test-union-all.R
/usr/lib64/R/library/dplyr/tests/testthat/test-utils.R
/usr/lib64/R/library/dplyr/tests/testthat/test-window.R
/usr/lib64/R/library/dplyr/tests/testthat/utf-8.txt

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/dplyr/libs/dplyr.so
/usr/lib64/R/library/dplyr/libs/dplyr.so.avx2
/usr/lib64/R/library/dplyr/libs/dplyr.so.avx512
