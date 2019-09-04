wget "https://www.xfitter.org/xFitter/xFitter/DownloadPage?action=AttachFile&do=get&target=xfitter-2.0.1.tgz" -O xfitter.tgz
tar -xzf xfitter.tgz

p=$PWD
mkdir xfitterBuild
cd xfitter-2.0.1

sed -i 's/-std=c++11/-std=c++17/' configure.ac

#libTool black magic
libtoolize
aclocal
autoreconf -i

./configure --prefix=$p/xfitterBuild  --enable-lhapdf --disable-applgrid

cp /afs/desy.de/user/z/zlebcr/h1/dfitter/xfitter-2.0.0/FastNLO/src/*.cc                xfitter-2.0.1/FastNLO/src/
cp /afs/desy.de/user/z/zlebcr/h1/dfitter/xfitter-2.0.0/FastNLO/include/*.h             xfitter-2.0.1/FastNLO/include/
cp /afs/desy.de/user/z/zlebcr/h1/dfitter/xfitter-2.0.0/FastNLO/include/fastnlotk/*.h   xfitter-2.0.1/FastNLO/include/fastnlotk
cp /afs/desy.de/user/z/zlebcr/h1/dfitter/xfitter-2.0.0/FastNLO/include/fastnlotk/*.hpp xfitter-2.0.1/FastNLO/include/fastnlotk


make -j`npoc`
make install
