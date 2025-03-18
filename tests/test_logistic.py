"""
测试Logistic映射代码
"""

import numpy as np
import pytest
import matplotlib.pyplot as plt
#from solutions.logistic_map_solution import iterate_logistic, plot_time_series, plot_bifurcation
from src.logistic_map_student import iterate_logistic, plot_time_series, plot_bifurcation

def test_iterate_logistic():
    """测试Logistic迭代函数"""
    # 测试r=2时的稳定点
    x = iterate_logistic(2.0, 0.5, 100)
    assert abs(x[-1] - 0.5) < 1e-6, "r=2时应收敛到0.5"
    
    # 测试值域
    x = iterate_logistic(3.2, 0.5, 100)
    assert np.all((x >= 0) & (x <= 1)), "所有值应在[0,1]范围内"
    
    # 测试周期性
    # 测试周期性 - 检查是否为周期4，而不是检查具体的排列
    x = iterate_logistic(3.5, 0.5, 200)
    period = x[-8:]  # 取最后8个点
    assert np.allclose(period[:4], period[4:], rtol=1e-2), "r=3.5时应为周期4"
    
    # 或者方法2：检查是否为周期4，而不是检查具体的排列
    # x = iterate_logistic(3.45, 0.5, 200)
    # period = x[-8:]  # 取最后8个点
    # assert np.allclose(period[:4], period[4:], rtol=1e-2), "r=3.45时应为周期4"

def test_plot_time_series():
    """测试时间序列绘图函数"""
    fig = plot_time_series(3.2, 0.5, 100)
    
    # 检查返回值类型
    assert isinstance(fig, plt.Figure)
    
    # 检查图像内容
    ax = fig.get_axes()[0]
    assert len(ax.get_lines()) == 1, "应该只有一条线"
    assert ax.get_xlabel() != "", "应该有x轴标签"
    assert ax.get_ylabel() != "", "应该有y轴标签"
    
    plt.close(fig)

def test_plot_bifurcation():
    """测试分岔图绘制函数"""
    fig = plot_bifurcation(3.0, 3.6, 100, 100, 50)
    
    # 检查返回值类型
    assert isinstance(fig, plt.Figure)
    
    # 检查图像内容
    ax = fig.get_axes()[0]
    assert ax.get_xlabel() != "", "应该有x轴标签"
    assert ax.get_ylabel() != "", "应该有y轴标签"
    
    plt.close(fig)

if __name__ == "__main__":
    pytest.main(["-v", __file__])