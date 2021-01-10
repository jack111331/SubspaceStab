//
// Created by yanhang on 4/21/16.
//

#ifndef SUBSPACESTAB_TRACKING_H
#define SUBSPACESTAB_TRACKING_H

#include <opencv2/opencv.hpp>
#include <Eigen/Eigen>
#include <vector>
#include <string>
#include <glog/logging.h>

namespace substab {
    struct FeatureTracks{
        std::vector<std::vector<cv::Point2f> > tracks;
        std::vector<size_t> offset;
    };

    struct KLTSetting {
        double quality_level;
        double min_distance;
        int winSizePyramid;
        int nLevel;
    };

    struct OpticalFlowSetting {
        double max_diff_distance;
        int max_corners;
        int interval;
    };

    struct TrackingSetting {
        struct KLTSetting kltSetting;
        struct OpticalFlowSetting ofSetting;
    };

    namespace Tracking {
        void genTrackMatrix(const std::vector<cv::Mat>& images, FeatureTracks& trackMatrix, const int tWindow, const int stride, const TrackingSetting &trackSetting);
        void filterDynamicTracks(FeatureTracks& trackMatrix, const int N);

        void visualizeTrack(const std::vector<cv::Mat>& images, const FeatureTracks& trackMatrix, const int startFrame);
    }
}
#endif //SUBSPACESTAB_TRACKING_H
