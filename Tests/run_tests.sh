EXAMPLES_DIR="/Users/linus/Dropbox/projects/collectiveBehaviour/wormtracking/Multiworm_Tracking/Tests"
SCRIPT_DIR=/Users/linus/Dropbox/projects/collectiveBehaviour/wormtracking/Multiworm_Tracking/cmd_scripts

TEST1_DIR="$EXAMPLES_DIR/test_1"
TEST2_DIR="$EXAMPLES_DIR/test_2"
TEST3_DIR="$EXAMPLES_DIR/test_3"
TEST4_DIR="$EXAMPLES_DIR/test_4"
TEST5_DIR="$EXAMPLES_DIR/test_5"

function test1 {
echo "%%%% TEST1 %%%%"
chflags -R nouchg "$TEST1_DIR/MaskedVideos"
rm -Rf "$TEST1_DIR/MaskedVideos"
python3  "$SCRIPT_DIR/compressMultipleFiles.py" "$TEST1_DIR/RawVideos" "$TEST1_DIR/MaskedVideos"
}

function test2 {
echo "%%%% TEST2 %%%%"
chflags -R nouchg "$TEST2_DIR/MaskedVideos"
rm -Rf "$TEST2_DIR/MaskedVideos"

python3  "$SCRIPT_DIR/compressMultipleFiles.py" "$TEST2_DIR/RawVideos" "$TEST2_DIR/MaskedVideos" \
--json_file "$TEST2_DIR/test2.json" --pattern_include "*.avi"
}

function test3 {
echo "%%%% TEST3 %%%%"
rm -Rf "$TEST3_DIR/Results"
python3  "$SCRIPT_DIR/trackMultipleFiles.py" "$TEST3_DIR/MaskedVideos" --json_file "$TEST3_DIR/test3.json"
}

function test4 {
echo "%%%% TEST4 %%%%"
rm "$TEST4_DIR/Results/Capture_Ch1_18062015_140908_feat_manual.hdf5"
python3  "$SCRIPT_DIR/trackMultipleFiles.py" "$TEST4_DIR/MaskedVideos" --json_file "$TEST3_DIR/test3.json" \
--use_manual_join
}

function test5 {
echo "%%%% TEST5 %%%%"
rm -Rf "$TEST5_DIR/Results"
python3  "$SCRIPT_DIR/trackMultipleFiles.py" "$TEST5_DIR/MaskedVideos"
}
function clean_all {
rm -Rf "$TEST1_DIR/MaskedVideos"
rm -Rf "$TEST2_DIR/MaskedVideos"
rm -Rf "$TEST3_DIR/Results"
}

test1
test2
test3
test4
test5