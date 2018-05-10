#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dplyr
Version  : 0.7.4
Release  : 13
URL      : https://cran.r-project.org/src/contrib/dplyr_0.7.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dplyr_0.7.4.tar.gz
Summary  : A Grammar of Data Manipulation
Group    : Development/Tools
License  : MIT
Requires: R-dplyr-lib
Requires: R-BH
Requires: R-Rcpp
Requires: R-assertthat
Requires: R-bindrcpp
Requires: R-glue
Requires: R-pkgconfig
Requires: R-plogr
Requires: R-tibble
BuildRequires : R-BH
BuildRequires : R-Rcpp
BuildRequires : R-assertthat
BuildRequires : R-bindrcpp
BuildRequires : R-glue
BuildRequires : R-pkgconfig
BuildRequires : R-plogr
BuildRequires : R-tibble
BuildRequires : clr-R-helpers

%description
both in memory and out of memory.

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
export SOURCE_DATE_EPOCH=1523303822

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523303822
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
/usr/lib64/R/library/dplyr/help/figures/logo.png
/usr/lib64/R/library/dplyr/help/paths.rds
/usr/lib64/R/library/dplyr/html/00Index.html
/usr/lib64/R/library/dplyr/html/R.css
/usr/lib64/R/library/dplyr/include/dplyr.h
/usr/lib64/R/library/dplyr/include/dplyr/BoolResult.h
/usr/lib64/R/library/dplyr/include/dplyr/CharacterVectorOrderer.h
/usr/lib64/R/library/dplyr/include/dplyr/Collecter.h
/usr/lib64/R/library/dplyr/include/dplyr/Column.h
/usr/lib64/R/library/dplyr/include/dplyr/DataFrameColumnSubsetVisitor.h
/usr/lib64/R/library/dplyr/include/dplyr/DataFrameColumnVisitor.h
/usr/lib64/R/library/dplyr/include/dplyr/DataFrameJoinVisitors.h
/usr/lib64/R/library/dplyr/include/dplyr/DataFrameSubsetVisitors.h
/usr/lib64/R/library/dplyr/include/dplyr/DataFrameVisitors.h
/usr/lib64/R/library/dplyr/include/dplyr/DataFrameVisitorsIndexMap.h
/usr/lib64/R/library/dplyr/include/dplyr/EmptySubset.h
/usr/lib64/R/library/dplyr/include/dplyr/FullDataFrame.h
/usr/lib64/R/library/dplyr/include/dplyr/Gatherer.h
/usr/lib64/R/library/dplyr/include/dplyr/GroupedDataFrame.h
/usr/lib64/R/library/dplyr/include/dplyr/Groups.h
/usr/lib64/R/library/dplyr/include/dplyr/Hybrid.h
/usr/lib64/R/library/dplyr/include/dplyr/HybridHandler.h
/usr/lib64/R/library/dplyr/include/dplyr/HybridHandlerMap.h
/usr/lib64/R/library/dplyr/include/dplyr/JoinVisitor.h
/usr/lib64/R/library/dplyr/include/dplyr/JoinVisitorImpl.h
/usr/lib64/R/library/dplyr/include/dplyr/MatrixColumnSubsetVectorVisitor.h
/usr/lib64/R/library/dplyr/include/dplyr/MatrixColumnVisitor.h
/usr/lib64/R/library/dplyr/include/dplyr/MultipleVectorVisitors.h
/usr/lib64/R/library/dplyr/include/dplyr/NamedListAccumulator.h
/usr/lib64/R/library/dplyr/include/dplyr/Order.h
/usr/lib64/R/library/dplyr/include/dplyr/OrderVisitor.h
/usr/lib64/R/library/dplyr/include/dplyr/OrderVisitorImpl.h
/usr/lib64/R/library/dplyr/include/dplyr/Replicator.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/CallElementProxy.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/CallProxy.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/CallbackProcessor.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/ConstantResult.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/Count.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/Count_Distinct.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/CumMax.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/CumMin.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/CumSum.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/DelayedProcessor.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/GroupedCallProxy.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/GroupedCallReducer.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/GroupedHybridCall.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/GroupedSubset.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/GroupedSubsetBase.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/ILazySubsets.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/In.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/Lag.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/LazyGroupedSubsets.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/LazyRowwiseSubsets.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/LazySubsets.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/Lead.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/Mean.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/MinMax.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/Mutater.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/Processor.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/Rank.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/Result.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/RowwiseSubset.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/Sd.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/Sum.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/Var.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/VectorSliceVisitor.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/all.h
/usr/lib64/R/library/dplyr/include/dplyr/Result/is_smaller.h
/usr/lib64/R/library/dplyr/include/dplyr/RowwiseDataFrame.h
/usr/lib64/R/library/dplyr/include/dplyr/SubsetVectorVisitor.h
/usr/lib64/R/library/dplyr/include/dplyr/SubsetVectorVisitorImpl.h
/usr/lib64/R/library/dplyr/include/dplyr/SummarisedVariable.h
/usr/lib64/R/library/dplyr/include/dplyr/VectorVisitor.h
/usr/lib64/R/library/dplyr/include/dplyr/VectorVisitorImpl.h
/usr/lib64/R/library/dplyr/include/dplyr/bad.h
/usr/lib64/R/library/dplyr/include/dplyr/checks.h
/usr/lib64/R/library/dplyr/include/dplyr/comparisons.h
/usr/lib64/R/library/dplyr/include/dplyr/config.h
/usr/lib64/R/library/dplyr/include/dplyr/dplyr.h
/usr/lib64/R/library/dplyr/include/dplyr/get_column.h
/usr/lib64/R/library/dplyr/include/dplyr/join_match.h
/usr/lib64/R/library/dplyr/include/dplyr/main.h
/usr/lib64/R/library/dplyr/include/dplyr/registration.h
/usr/lib64/R/library/dplyr/include/dplyr/subset_visitor.h
/usr/lib64/R/library/dplyr/include/dplyr/subset_visitor_impl.h
/usr/lib64/R/library/dplyr/include/dplyr/tbl_cpp.h
/usr/lib64/R/library/dplyr/include/dplyr/train.h
/usr/lib64/R/library/dplyr/include/dplyr/vector_class.h
/usr/lib64/R/library/dplyr/include/dplyr/visitor.h
/usr/lib64/R/library/dplyr/include/dplyr/visitor_impl.h
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
/usr/lib64/R/library/dplyr/include/dplyr/visitor_set/VisitorSetMixin.h
/usr/lib64/R/library/dplyr/include/dplyr/visitor_set/visitor_set.h
/usr/lib64/R/library/dplyr/include/dplyr/white_list.h
/usr/lib64/R/library/dplyr/include/dplyr/workarounds.h
/usr/lib64/R/library/dplyr/include/dplyr/workarounds/static_assert.h
/usr/lib64/R/library/dplyr/include/dplyr/workarounds/xlen.h
/usr/lib64/R/library/dplyr/include/dplyr_RcppExports.h
/usr/lib64/R/library/dplyr/include/dplyr_types.h
/usr/lib64/R/library/dplyr/include/solaris/solaris.h
/usr/lib64/R/library/dplyr/include/tools/Call.h
/usr/lib64/R/library/dplyr/include/tools/Quosure.h
/usr/lib64/R/library/dplyr/include/tools/ShrinkableVector.h
/usr/lib64/R/library/dplyr/include/tools/SlicingIndex.h
/usr/lib64/R/library/dplyr/include/tools/SymbolMap.h
/usr/lib64/R/library/dplyr/include/tools/SymbolString.h
/usr/lib64/R/library/dplyr/include/tools/SymbolVector.h
/usr/lib64/R/library/dplyr/include/tools/all_na.h
/usr/lib64/R/library/dplyr/include/tools/collapse.h
/usr/lib64/R/library/dplyr/include/tools/debug.h
/usr/lib64/R/library/dplyr/include/tools/encoding.h
/usr/lib64/R/library/dplyr/include/tools/hash.h
/usr/lib64/R/library/dplyr/include/tools/match.h
/usr/lib64/R/library/dplyr/include/tools/pointer_vector.h
/usr/lib64/R/library/dplyr/include/tools/rlang-export.h
/usr/lib64/R/library/dplyr/include/tools/scalar_type.h
/usr/lib64/R/library/dplyr/include/tools/tools.h
/usr/lib64/R/library/dplyr/include/tools/utils.h
/usr/lib64/R/library/dplyr/include/tools/wrap_subset.h
/usr/lib64/R/library/dplyr/tests/testthat.R
/usr/lib64/R/library/dplyr/tests/testthat/helper-astyle.R
/usr/lib64/R/library/dplyr/tests/testthat/helper-combine.R
/usr/lib64/R/library/dplyr/tests/testthat/helper-encoding.R
/usr/lib64/R/library/dplyr/tests/testthat/helper-groups.R
/usr/lib64/R/library/dplyr/tests/testthat/helper-hybrid.R
/usr/lib64/R/library/dplyr/tests/testthat/helper-torture.R
/usr/lib64/R/library/dplyr/tests/testthat/test-DBI.R
/usr/lib64/R/library/dplyr/tests/testthat/test-arrange.r
/usr/lib64/R/library/dplyr/tests/testthat/test-astyle.R
/usr/lib64/R/library/dplyr/tests/testthat/test-between.R
/usr/lib64/R/library/dplyr/tests/testthat/test-binds.R
/usr/lib64/R/library/dplyr/tests/testthat/test-case-when.R
/usr/lib64/R/library/dplyr/tests/testthat/test-coalesce.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-arrange.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-filter.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-group-by.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-mutate.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-select.R
/usr/lib64/R/library/dplyr/tests/testthat/test-combine.R
/usr/lib64/R/library/dplyr/tests/testthat/test-copy_to.R
/usr/lib64/R/library/dplyr/tests/testthat/test-copying.R
/usr/lib64/R/library/dplyr/tests/testthat/test-count-tally.r
/usr/lib64/R/library/dplyr/tests/testthat/test-data_frame.R
/usr/lib64/R/library/dplyr/tests/testthat/test-distinct.R
/usr/lib64/R/library/dplyr/tests/testthat/test-do.R
/usr/lib64/R/library/dplyr/tests/testthat/test-equality.r
/usr/lib64/R/library/dplyr/tests/testthat/test-filter.r
/usr/lib64/R/library/dplyr/tests/testthat/test-funs-predicates.R
/usr/lib64/R/library/dplyr/tests/testthat/test-funs.R
/usr/lib64/R/library/dplyr/tests/testthat/test-group-by.r
/usr/lib64/R/library/dplyr/tests/testthat/test-group-indices.R
/usr/lib64/R/library/dplyr/tests/testthat/test-group-size.R
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
/usr/lib64/R/library/dplyr/tests/testthat/test-nth-value.R
/usr/lib64/R/library/dplyr/tests/testthat/test-overscope.R
/usr/lib64/R/library/dplyr/tests/testthat/test-pull.R
/usr/lib64/R/library/dplyr/tests/testthat/test-rank.R
/usr/lib64/R/library/dplyr/tests/testthat/test-rbind.R
/usr/lib64/R/library/dplyr/tests/testthat/test-recode.R
/usr/lib64/R/library/dplyr/tests/testthat/test-sample.R
/usr/lib64/R/library/dplyr/tests/testthat/test-select-helpers.R
/usr/lib64/R/library/dplyr/tests/testthat/test-select.r
/usr/lib64/R/library/dplyr/tests/testthat/test-sets.R
/usr/lib64/R/library/dplyr/tests/testthat/test-slice.r
/usr/lib64/R/library/dplyr/tests/testthat/test-summarise.r
/usr/lib64/R/library/dplyr/tests/testthat/test-tbl-cube.R
/usr/lib64/R/library/dplyr/tests/testthat/test-tbl.R
/usr/lib64/R/library/dplyr/tests/testthat/test-top-n.R
/usr/lib64/R/library/dplyr/tests/testthat/test-ts.R
/usr/lib64/R/library/dplyr/tests/testthat/test-underscore.R
/usr/lib64/R/library/dplyr/tests/testthat/test-union-all.R
/usr/lib64/R/library/dplyr/tests/testthat/test-utils.R
/usr/lib64/R/library/dplyr/tests/testthat/test-window.R
/usr/lib64/R/library/dplyr/tests/testthat/utf-8.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/dplyr/libs/dplyr.so
/usr/lib64/R/library/dplyr/libs/dplyr.so.avx2
/usr/lib64/R/library/dplyr/libs/dplyr.so.avx512
