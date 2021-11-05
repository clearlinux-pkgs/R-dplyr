#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dplyr
Version  : 1.0.7
Release  : 61
URL      : https://cran.r-project.org/src/contrib/dplyr_1.0.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dplyr_1.0.7.tar.gz
Summary  : A Grammar of Data Manipulation
Group    : Development/Tools
License  : MIT
Requires: R-dplyr-lib = %{version}-%{release}
Requires: R-R6
Requires: R-ellipsis
Requires: R-generics
Requires: R-glue
Requires: R-lifecycle
Requires: R-magrittr
Requires: R-pillar
Requires: R-rlang
Requires: R-tibble
Requires: R-tidyselect
Requires: R-vctrs
BuildRequires : R-R6
BuildRequires : R-ellipsis
BuildRequires : R-generics
BuildRequires : R-glue
BuildRequires : R-lifecycle
BuildRequires : R-magrittr
BuildRequires : R-pillar
BuildRequires : R-rlang
BuildRequires : R-tibble
BuildRequires : R-tidyselect
BuildRequires : R-vctrs
BuildRequires : buildreq-R

%description
like objects, both in memory and out of memory.

%package lib
Summary: lib components for the R-dplyr package.
Group: Libraries

%description lib
lib components for the R-dplyr package.


%prep
%setup -q -c -n dplyr
cd %{_builddir}/dplyr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624292219

%install
export SOURCE_DATE_EPOCH=1624292219
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
/usr/lib64/R/library/dplyr/doc/base.R
/usr/lib64/R/library/dplyr/doc/base.Rmd
/usr/lib64/R/library/dplyr/doc/base.html
/usr/lib64/R/library/dplyr/doc/colwise.R
/usr/lib64/R/library/dplyr/doc/colwise.Rmd
/usr/lib64/R/library/dplyr/doc/colwise.html
/usr/lib64/R/library/dplyr/doc/compatibility.R
/usr/lib64/R/library/dplyr/doc/compatibility.Rmd
/usr/lib64/R/library/dplyr/doc/compatibility.html
/usr/lib64/R/library/dplyr/doc/dplyr.R
/usr/lib64/R/library/dplyr/doc/dplyr.Rmd
/usr/lib64/R/library/dplyr/doc/dplyr.html
/usr/lib64/R/library/dplyr/doc/grouping.R
/usr/lib64/R/library/dplyr/doc/grouping.Rmd
/usr/lib64/R/library/dplyr/doc/grouping.html
/usr/lib64/R/library/dplyr/doc/index.html
/usr/lib64/R/library/dplyr/doc/programming.R
/usr/lib64/R/library/dplyr/doc/programming.Rmd
/usr/lib64/R/library/dplyr/doc/programming.html
/usr/lib64/R/library/dplyr/doc/rowwise.R
/usr/lib64/R/library/dplyr/doc/rowwise.Rmd
/usr/lib64/R/library/dplyr/doc/rowwise.html
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
/usr/lib64/R/library/dplyr/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/dplyr/help/figures/logo.png
/usr/lib64/R/library/dplyr/help/paths.rds
/usr/lib64/R/library/dplyr/html/00Index.html
/usr/lib64/R/library/dplyr/html/R.css
/usr/lib64/R/library/dplyr/tests/testthat.R
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/across.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/all-equal.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/arrange.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/bind.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/case-when.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/coalesce.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/colwise-filter.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/colwise-mutate.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/colwise-select.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/colwise.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/context.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/count-tally.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/deprec-combine.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/deprec-dbi.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/deprec-do.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/deprec-funs.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/deprec-src-local.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/distinct.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/filter.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/funs-predicates.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/group-by.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/group_map.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/grouped-df.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/if-else.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/join-cols.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/join-rows.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/lead-lag.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/mutate.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/na-if.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/nth-value.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/order-by.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/recode.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/rows.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/rowwise.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/sample.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/select.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/sets.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/slice.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/summarise.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/top-n.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/transmute.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/utils.md
/usr/lib64/R/library/dplyr/tests/testthat/_snaps/window.md
/usr/lib64/R/library/dplyr/tests/testthat/helper-dplyr.R
/usr/lib64/R/library/dplyr/tests/testthat/helper-encoding.R
/usr/lib64/R/library/dplyr/tests/testthat/helper-s3.R
/usr/lib64/R/library/dplyr/tests/testthat/helper-torture.R
/usr/lib64/R/library/dplyr/tests/testthat/test-DBI.R
/usr/lib64/R/library/dplyr/tests/testthat/test-across.R
/usr/lib64/R/library/dplyr/tests/testthat/test-all-equal.r
/usr/lib64/R/library/dplyr/tests/testthat/test-arrange.r
/usr/lib64/R/library/dplyr/tests/testthat/test-bind.R
/usr/lib64/R/library/dplyr/tests/testthat/test-case-when.R
/usr/lib64/R/library/dplyr/tests/testthat/test-coalesce.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-arrange.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-distinct.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-filter.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-funs.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-group-by.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-mutate.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise-select.R
/usr/lib64/R/library/dplyr/tests/testthat/test-colwise.R
/usr/lib64/R/library/dplyr/tests/testthat/test-context.R
/usr/lib64/R/library/dplyr/tests/testthat/test-count-tally.r
/usr/lib64/R/library/dplyr/tests/testthat/test-deprec-combine.R
/usr/lib64/R/library/dplyr/tests/testthat/test-deprec-dbi.R
/usr/lib64/R/library/dplyr/tests/testthat/test-deprec-do.R
/usr/lib64/R/library/dplyr/tests/testthat/test-deprec-funs.R
/usr/lib64/R/library/dplyr/tests/testthat/test-deprec-lazyeval.R
/usr/lib64/R/library/dplyr/tests/testthat/test-deprec-src-local.r
/usr/lib64/R/library/dplyr/tests/testthat/test-deprec-tibble.R
/usr/lib64/R/library/dplyr/tests/testthat/test-distinct.R
/usr/lib64/R/library/dplyr/tests/testthat/test-empty-groups.R
/usr/lib64/R/library/dplyr/tests/testthat/test-filter.r
/usr/lib64/R/library/dplyr/tests/testthat/test-funs-predicates.R
/usr/lib64/R/library/dplyr/tests/testthat/test-funs.R
/usr/lib64/R/library/dplyr/tests/testthat/test-generics.R
/usr/lib64/R/library/dplyr/tests/testthat/test-group-by.r
/usr/lib64/R/library/dplyr/tests/testthat/test-group_data.R
/usr/lib64/R/library/dplyr/tests/testthat/test-group_map.R
/usr/lib64/R/library/dplyr/tests/testthat/test-group_nest.R
/usr/lib64/R/library/dplyr/tests/testthat/test-group_split.R
/usr/lib64/R/library/dplyr/tests/testthat/test-group_trim.R
/usr/lib64/R/library/dplyr/tests/testthat/test-grouped-df.r
/usr/lib64/R/library/dplyr/tests/testthat/test-groups-with.R
/usr/lib64/R/library/dplyr/tests/testthat/test-if-else.R
/usr/lib64/R/library/dplyr/tests/testthat/test-join-cols.R
/usr/lib64/R/library/dplyr/tests/testthat/test-join-rows.R
/usr/lib64/R/library/dplyr/tests/testthat/test-join.r
/usr/lib64/R/library/dplyr/tests/testthat/test-lead-lag.R
/usr/lib64/R/library/dplyr/tests/testthat/test-mutate-windowed.R
/usr/lib64/R/library/dplyr/tests/testthat/test-mutate.r
/usr/lib64/R/library/dplyr/tests/testthat/test-n_distinct.R
/usr/lib64/R/library/dplyr/tests/testthat/test-na-if.R
/usr/lib64/R/library/dplyr/tests/testthat/test-near.R
/usr/lib64/R/library/dplyr/tests/testthat/test-nest_by.R
/usr/lib64/R/library/dplyr/tests/testthat/test-nth-value.R
/usr/lib64/R/library/dplyr/tests/testthat/test-order-by.R
/usr/lib64/R/library/dplyr/tests/testthat/test-pull.R
/usr/lib64/R/library/dplyr/tests/testthat/test-rank.R
/usr/lib64/R/library/dplyr/tests/testthat/test-rbind.R
/usr/lib64/R/library/dplyr/tests/testthat/test-recode.R
/usr/lib64/R/library/dplyr/tests/testthat/test-relocate.R
/usr/lib64/R/library/dplyr/tests/testthat/test-rename.R
/usr/lib64/R/library/dplyr/tests/testthat/test-rows.R
/usr/lib64/R/library/dplyr/tests/testthat/test-rowwise.r
/usr/lib64/R/library/dplyr/tests/testthat/test-sample.R
/usr/lib64/R/library/dplyr/tests/testthat/test-select-helpers.R
/usr/lib64/R/library/dplyr/tests/testthat/test-select.r
/usr/lib64/R/library/dplyr/tests/testthat/test-sets.R
/usr/lib64/R/library/dplyr/tests/testthat/test-slice.r
/usr/lib64/R/library/dplyr/tests/testthat/test-summarise.r
/usr/lib64/R/library/dplyr/tests/testthat/test-tbl.R
/usr/lib64/R/library/dplyr/tests/testthat/test-top-n.R
/usr/lib64/R/library/dplyr/tests/testthat/test-transmute.R
/usr/lib64/R/library/dplyr/tests/testthat/test-union-all.R
/usr/lib64/R/library/dplyr/tests/testthat/test-utils.R
/usr/lib64/R/library/dplyr/tests/testthat/test-window.R
/usr/lib64/R/library/dplyr/tests/testthat/utf-8.txt

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/dplyr/libs/dplyr.so
/usr/lib64/R/library/dplyr/libs/dplyr.so.avx2
/usr/lib64/R/library/dplyr/libs/dplyr.so.avx512
