Synopsys support files Non-Interactive Flow
=======================

Support files for setting up the technology on Synospys Flow
Alpha quality, provided as-is, no guarantees.

```bash
# To clone the directory, checkout with "main" and install pre-required tools:
./make_run.sh

# Make it writeable

chmod 777 -R ../skywaterlib-synopsysdb

# To build skywater-PDK to generate synopsys libraries
python3 libtodb.py

```

Directory structure
--------------------

```pre
skywater-PDK
└── vendor/
    └── synopsys/
        ├── Makefile
        ├── scripts     : Common script to gnerated SNPS libraries
        ├── work        : Work directory while creating libraries
        ├── logs        : Stored logs
        └── PlaceRoute/
            └── common          : Common files
            └── $SC_LIB_NAME/
                ├── -NDM        : Final NDM to use with SNPS flow
                ├── -db_nldm    : Compiled DB files
                ├── -lib        : Fixed lib files
                ├── -techfile   : .tf and supported files
                ├── -lef        : Modified/Regenerated LEF Files
                ├── -gds        : Symbolic link of gds files
                ├── -verilog    : Fixed verilog, if required
                └── -others     : reserved
```

**Note**:
In `PlaceRoute/common` directory contains following 3 pre compiled files.

```pre
- sky130_fd_sc_hd.antenna.clf
- skywater130.mw2itf.map
- skywater130.mw.map
```

**Courtesy**:

https://github.com/ganeshgore/skywater-pdk
