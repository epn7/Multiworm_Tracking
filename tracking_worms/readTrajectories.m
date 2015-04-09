segworm_file = '/Volumes/behavgenom$/syngenta/Trajectories/data_20150114/compound_a_repeat_2_fri_5th_dec_segworm.hdf5';
trajectories_file = '/Volumes/behavgenom$/syngenta/Trajectories/data_20150114/compound_a_repeat_2_fri_5th_dec_trajectories.hdf5';

%read trajectories data
trajectories_data = h5read(trajectories_file, '/plate_worms');

%read all data files in teh segworm_file. An alternative, if only the skeleton
%is need, would be just to use:
% h5read(segworm_file, '/segworm_results/skeleton');

segworm_headers = h5info(segworm_file);
strFields = cell(1,numel(segworm_headers.Groups.Datasets));
for kk = 1:numel(segworm_headers.Groups.Datasets)
    strFields{kk} = segworm_headers.Groups.Datasets(kk).Name;
end
segworm_data = [];
for ff = strFields
    segworm_data.(ff{1}) = h5read(segworm_file, ['/segworm_results/' ff{1}]);
end

%% Plot the displacement of the center of mass
valid_index = unique(trajectories_data.worm_index_joined)';
valid_index(valid_index<=0) = [];

%figure, hold on
for ind = valid_index
    good = trajectories_data.worm_index_joined == ind;
    
    xx = trajectories_data.coord_x(good);
    yy = trajectories_data.coord_y(good);
    plot(xx,yy)
end
axis equal
title('CM Trajectories')
%% Plot all the individual skeletons
%trajectories_data.segworm_id is the corresponding row in any  of the
%fields in segworm_data. If the value is -1 this means segworm failed 
%for that particular frame/ROI.

valid_index = unique(trajectories_data.worm_index_joined(trajectories_data.segworm_id>=0))';
valid_index(valid_index<=0) = [];

figure, hold on
for ind = valid_index
    good = trajectories_data.worm_index_joined == ind;
    segworm_row = trajectories_data.segworm_id(good)+1; %python indexing add one
    segworm_row(segworm_row<=0) = [];
    
    strC = rand(1,3);
    for row = segworm_row'
        dat = segworm_data.skeleton(:,:,row);
        plot(dat(:,2),dat(:,1), 'color', strC)
    end
end
axis equal
title('Segworm Skeletons')

