#ifndef __CREATE_POOLING_NODE_HPP__
#define __CREATE_POOLING_NODE_HPP__


namespace tensorrtInference
{
    extern nvinfer1::ILayer* createPoolingNode(nvinfer1::INetworkDefinition* network, std::map<std::string, nvinfer1::ITensor*>& tensors,  
        tensorrtInference::nodeInfo* nodeConfInfo, std::map<std::string, tensorrtInference::weightInfo>& nodeWeightsInfo);
}

#endif